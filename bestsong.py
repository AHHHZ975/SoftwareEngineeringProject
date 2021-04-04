from db import mongo

class BestSong():
    def getBetsSongTitle():    
        bestViews = []
        bestTitles = []
        musics = mongo.db.musics.find({})
        for music in musics:
            bestTitles.append(music['title'])
            bestViews.append(music['view'])
        
        # for j in range(len(title)):
        #     weight.append((float(likes[j]) / float(max(likes)) * 5) + float(rates[j]))
        # print(sorted(zip(bestViews, bestTitles), reverse=True)[:2])
        bests = sorted(zip(bestViews, bestTitles), reverse=True) 
        sortedBestTitles = []
        for best in bests:
            sortedBestTitles.append(best[1])
        return sortedBestTitles
        