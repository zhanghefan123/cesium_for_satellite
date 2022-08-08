import tle2czml
from datetime import datetime
# You can specify the time range you would like to visualise
start_time = datetime(2020, 10, 1, 17, 30)
end_time = datetime(2020, 10, 2, 19, 30)
tle2czml.create_czml("./test/iridium.txt", start_time=start_time, end_time=end_time, outputfile_path="./Apps/SampleData/iridium.czml")