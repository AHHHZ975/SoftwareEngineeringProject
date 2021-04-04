import flask
from utils import login_required
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
import time

class Search(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('search.html')
        
    @login_required
    def post(self):
        searchText = flask.request.form['expression']        
        self.getMusic(searchText)
        self.getMusicInformation(searchText)
        # flask.flash(searchText)
        return flask.redirect(flask.url_for('search'))
    
    @login_required
    def getMusic(self, searchText):
        # downloading music
        songLimit = 1 
        url = 'https://freemp3cloud.com/'

        out = []
        driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
        driver.get(url)
        searchbox  = driver.find_element_by_id('searchSong') 
        searchbox.click()
        searchbox.send_keys(searchText)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(2)

        links = driver.find_elements_by_class_name("pi-data")
        count = 0
        for link in links:
            try:
                att = {}
                artist = link.find_element_by_class_name("s-artist").text 
                title = link.find_element_by_class_name("s-title").text
                times = link.find_element_by_class_name("s-time").text
                download_link = link.find_element_by_tag_name("a").get_attribute('href')
                att['artist'] = artist
                att['title'] = title
                att['time'] = times
                att['download_link'] = download_link
                count += 1                
            except:
                pass
            if att != {}:
                out.append(att)
            if count >= songLimit:
                break
        driver.close()


        # save in file
        import json
        with open('db/sounds.json', 'w') as f:
            json.dump(out, f, indent=4)
            print("output saved in the sound.json file")

    @login_required
    def getMusicInformation(self, searchText):
        # lyric parameters
        lyric_limit = 1
        lyric_url = "https://www.lyricfinder.org/search/lyrics/"
            
        url = lyric_url + searchText
        driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
        driver.get(url)
        out = []
        links = driver.find_elements_by_tag_name('p')
        count = 0
        for link in links:
            att = {}
            try: 
                title = link.find_element_by_class_name("song-title-link").text
                artist = link.find_element_by_class_name("artist-link").text
                lyric_link = link.find_element_by_class_name("song-title-link").get_attribute('href')
                att['lyric'] = lyric_link
                att['title'] = title
                att['artist'] = artist
                count += 1
            except:
                pass
            if att != {}:
                out.append(att)
            if count >= lyric_limit:
                break
        driver.close()

        # download lyric from text link
        for item in out:
            driver1 = webdriver.Firefox(executable_path=r'./geckodriver.exe')
            driver1.get(item['lyric'])
            lyric = driver1.find_element_by_class_name("col-lg-6").text
            driver1.close()
            item['lyric'] = lyric 
            
        # save in file
        import json
        with open('db/lyrics.json', 'w') as f:
            json.dump(out, f, indent=4)
            print("output saved in the lyrics.json file")