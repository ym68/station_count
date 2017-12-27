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

get the results both in the screen print and sum.csv for each SSID, AP_MAC, etc

if data cleaning is "Y", then you will need a file ana_cleaned.csv. "Y" means the End time is before whtat you expected. Remeber to copy and rename ana_cleaned_empty.csv to ana_cleaned.csv for the first using of ana_cleaned.csv, the purpose is the have the header with empty figures.  Then you can run  

python cleaned_count.py  

to get the results both in the screen print and sum.csv for the combined ana_cleaned.csv file.
