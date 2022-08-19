import urllib.request
from satellite_czml import satellite_czml
from datetime import datetime, timedelta
import random
url = 'https://celestrak.com/NORAD/elements/stations.txt'
tles = [l.decode("utf-8").strip() for l in urllib.request.urlopen(url).readlines()]
tle_list = [[tles[i],tles[i+1],tles[i+2]] for i,_ in enumerate(tles) if i%3==0]
small_tle_list = tle_list[:4]
for tle in small_tle_list:
  print(tle)

print("----------------------------------------------------------------------------")

single_tle = [tle_list[0]]
print(single_tle)

print("----------------------------------------------------------------------------")

single_czml = satellite_czml(tle_list=single_tle).get_czml()

fileName = './Apps/SampleData/simple.czml'
with open(fileName,'w') as file:
  file.write(single_czml)

name_list = [t[0] for t in small_tle_list] 
description_list = ['Station: ' + t[0] for t in small_tle_list]
color_list = [[random.randrange(256) for x in range(3)] for x in range(len(small_tle_list))]
size_list = [7] * len(small_tle_list)

czml_obj = satellite_czml(tle_list=small_tle_list, name_list=name_list, description_list=description_list,
                          color_list=color_list, speed_multiplier=1, use_default_image=False,
                          marker_scale_list=size_list, show_label=False, show_path=False,
                          ignore_bad_tles=True)
multiple_czml_p = czml_obj.get_czml()
fileName = './Apps/SampleData/multiple.czml'
with open(fileName,'w') as file:
  file.write(multiple_czml_p)

from satellite_czml import satellite

multiple_sats=[]
for tle in small_tle_list:
    sat = satellite(tle,
                    description='Station: ' + tle[0],
                    color = [random.randrange(256) for x in range(3)],
                    marker_scale=12,
                    use_default_image=False,
                    start_time=datetime.strptime('2020-01-01 00:00:00','%Y-%m-%d %H:%M:%S'),
                    end_time=datetime.strptime('2020-01-01 02:00:00','%Y-%m-%d %H:%M:%S'),
                    show_label=True,
                    show_path=True,
                   )
    multiple_sats.append(sat)
    

czml_obj = satellite_czml(satellite_list=multiple_sats)
multiple_czml_c = czml_obj.get_czml()

fileName = './Apps/SampleData/createOneByOne.czml'
with open(fileName,'w') as file:
  file.write(multiple_czml_c)