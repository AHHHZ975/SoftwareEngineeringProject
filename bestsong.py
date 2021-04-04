import json

def _decode(o):
    if isinstance(o, str) :
        try:
            return float(o)
        except ValueError:
            return o
    elif isinstance(o, dict):
        return {k: _decode(v) for k, v in o.items()}
    elif isinstance(o, list):
        return [_decode(v) for v in o]
    else:
        return o

with open('/Users/zoha/Desktop/songs.json') as f:
    songs = json.load(f, object_hook=_decode)

likes = []
rates = []
weight = []
names = []


for i in songs['details']:
    names.append(i['name'])
    likes.append(i['likes'])
    rates.append(i['rate'])

for j in range(len(names)):
    weight.append((float(likes[j]) / float(max(likes)) * 5) + float(rates[j]))

print(sorted(zip(weight, names), reverse=True)[:10])