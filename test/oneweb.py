import urllib.request
import numpy as np
from satellite_czml import satellite_czml
from datetime import datetime, timedelta
from satellite_czml import satellite
import random
url = 'https://celestrak.com/NORAD/elements/oneweb.txt'
tles = [l.decode("utf-8").strip() for l in urllib.request.urlopen(url).readlines()]
tle_list = [[tles[i],tles[i+1],tles[i+2]] for i,_ in enumerate(tles) if i%3==0]
# -----------------------------------first calculate------------------------------------------------------------------
multiple_sats=[]
for tle in tle_list:
    sat = satellite(tle,
                    description='Satellite: ' + tle[0],
                    color = [random.randrange(256) for x in range(3)],
                    marker_scale=10,
                    use_default_image=False,
                    start_time=datetime.strptime('2022-08-15 00:00:00','%Y-%m-%d %H:%M:%S'),
                    end_time=datetime.strptime('2022-08-15 02:00:00','%Y-%m-%d %H:%M:%S'),
                    show_label=True,
                    show_path=True,
                   )
    multiple_sats.append(sat)

czml_obj = satellite_czml(satellite_list=multiple_sats)
multiple_czml_c = czml_obj.get_czml()
# -----------------------------------calculate illegal satellites-----------------------------------------------------
illegal_satellites = []
for satelliteNum in czml_obj.satellites:
  if np.isnan(czml_obj.get_satellite(satelliteNum).czmlPosition.cartesian.data()).any():
    illegal_satellites.append(satelliteNum)
print(illegal_satellites)
# --------------------------------------------------------------------------------------------------------------------
multiple_sats=[]
for tle in tle_list:
    sat = satellite(tle,
                    description='Satellite: ' + tle[0],
                    color = [random.randrange(256) for x in range(3)],
                    marker_scale=10,
                    use_default_image=False,
                    start_time=datetime.strptime('2022-08-15 00:00:00','%Y-%m-%d %H:%M:%S'),
                    end_time=datetime.strptime('2022-08-15 02:00:00','%Y-%m-%d %H:%M:%S'),
                    show_label=True,
                    show_path=True,
                   )
    if sat.id in illegal_satellites:
      pass
    else:
      multiple_sats.append(sat)
print(len(multiple_sats))
satellite_czml.satellites = {}
czml_obj = satellite_czml(satellite_list=multiple_sats)
multiple_czml_c = czml_obj.get_czml()
fileName = './Apps/SampleData/oneweb.czml'
with open(fileName,'w') as file:
  file.write(multiple_czml_c)