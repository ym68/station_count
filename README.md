# station_count

## env preparation

virtualenv venpd

cd venpd

source ./bin/activate #Linux or

  cd scripts & activate #Windows

pip install pandas



## run data cleaning and analysis
save csv files under /csv and mind the path in station_count.py

copy .csv and rename as ana.csv

run
python station_count.py

follow the screen reminders for the SSID, AP_MAC, etc

if data cleaning is "Y", then you will get a file csv_cleaned.csv. Do the analysis with excel

for data within 10k lines, you can use the station_count.py completely and get the results both in the screen print and  sum.csv file.

