from db import mongo

songs = mongo.db.musics

view = []
title = []

for song in songs:
    title.append(song['title'])
    view.append(song['view'])

# for j in range(len(title)):
#     weight.append((float(likes[j]) / float(max(likes)) * 5) + float(rates[j]))

print(sorted(zip(view, title), reverse=True)[:1])