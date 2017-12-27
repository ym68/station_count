#!/usr/bin/python
# coding:utf-8

import pandas as pd


data = pd.read_csv('ana_cleaned.csv',skiprows=0)

data_c = data  #connected


count_Station = data_c['Station '].value_counts()  #quantity of each station(MP, customer)
Total_Station_No = len(count_Station) # duplicate removed
Total_Connection = len(data_c)


print('总计连接次数为: ', Total_Connection,'总计连接终端数为： ',Total_Station_No)

## Time & Period

Time_Start = data_c['Time'].min() 
Time_End = data_c['Time'].max()  

print('时间始于',Time_Start, '时间截止于',Time_End)


## cleaned csv

data_clean_to_csv = input('是否导出清洗过的csv文件： Y or N ? 回车为否。首次导出时记得使用带表头的空表 ana_cleaned (empty).csv, 更名为ana_cleaned.csv')

if data_clean_to_csv == 'N' or '':
    pass
else:
    cleaned_data = pd.DataFrame(data = data_c, columns=['Station ','SSID','AP MAC','Time','RSSI','Vendor'])  #ok
    cleaned_data.to_csv('ana_cleaned.csv',mode='a', header=False)


## SSID count

count_SSID = data_c['SSID'].value_counts()  #quantity of each station(MP, customer) under certain SSID

SSIDs = count_SSID.index

for SSID in SSIDs:
    print (SSID)
    if SSID == '':
        pass
    else:
        data_SSID = data[(data['SSID'] == SSID)] ## conected under certain AP MAC
        count_SSIDStation = data_SSID['Station '].value_counts()  #quantity of each station(MP, customer) under certain AP MAC
        SSID_Station_No = len(count_SSIDStation) # duplicate removed
        SSID_Total_Connection = len(data_SSID)
        print('SSID的总计连接次数为： ', SSID_Total_Connection,',占比为： %.3f ' %(SSID_Total_Connection/Total_Connection),'SSID',SSID,'的总计连接终端数为： ', SSID_Station_No,', 占比为：%.3f ' %(SSID_Station_No/Total_Station_No))
        rows = [(Time_Start,Time_End,Total_Connection,Total_Station_No, SSID,SSID_Total_Connection,SSID_Station_No)]
        df = pd.DataFrame(data=list(rows),columns=('时间始于', '时间截止于', '总计连接次数','总计连接终端数', 'SSID','SSID的总计连接次数','SSID的总计连接终端数'))
        df.to_csv('sum.csv',mode='a', header=True)






## AP count

count_AP_MAC = data_c['AP MAC'].value_counts()  #quantity of each station(MP, customer)

APs = count_AP_MAC.index

for AP in APs:
    print (AP)
    if AP == '':
        pass
    else:
        data_cap = data[(data['AP MAC'] == AP)] ## conected under certain AP MAC
        count_apStation = data_cap['Station '].value_counts()  #quantity of each station(MP, customer) under certain AP MAC
        AP_Station_No = len(count_apStation) # duplicate removed
        AP_Total_Connection = len(data_cap)
        print('AP的总计连接次数为： ', AP_Total_Connection,',占比为： %.3f ' %(AP_Total_Connection/Total_Connection),'AP',AP[12:],'的总计连接终端数为： ', AP_Station_No,', 占比为：%.3f ' %(AP_Station_No/Total_Station_No))
        rows = [(Time_Start,Time_End,Total_Connection,Total_Station_No, AP,AP_Total_Connection,AP_Station_No)]
        df = pd.DataFrame(data=list(rows),columns=('时间始于', '时间截止于', '总计连接次数','总计连接终端数', 'AP MAC', 'AP的总计连接次数','AP总计连接终端数'))
        df.to_csv('sum.csv',mode='a', header=True)



