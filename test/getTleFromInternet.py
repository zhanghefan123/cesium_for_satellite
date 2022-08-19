import urllib.request

url = 'https://celestrak.com/NORAD/elements/stations.txt'
tles = [l.decode("utf-8").strip() for l in urllib.request.urlopen(url).readlines()]
tle_list = [[tles[i],tles[i+1],tles[i+2]] for i,_ in enumerate(tles) if i%3==0]
small_tle_list = tle_list[:4]
for tle in small_tle_list:
  print(tle)