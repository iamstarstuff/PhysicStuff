import numpy as np 
import pandas as pd 
from datetime import datetime
import speedtest as st

# Run this cell only first time to create empty csv file then comment out the cell
# to avoid losing data
'''
create_df = pd.DataFrame(columns=["Date and Time","Download Speed (Mbps)","Upload Speed (Mbps)","Ping Speed (ms)"])
create_df.to_csv("SpeedData.csv",index=False)
'''

def getspeed():
    s = st.Speedtest()
    s.get_best_server()
    ping = s.results.ping
    down = round(s.download()/10**6,2) # Divide by 10**6 to converts bps to Mbps
    up = round(s.upload()/10**6,2)
    timestamp = datetime.now().strftime("%d/%b/%Y - %H:%M:%S IST")
    return (timestamp,down,up,ping)

def updatecsv(speed):
    new_entry = pd.DataFrame({'Date and Time':[speed[0]],'Download Speed (Mbps)':[speed[1]],'Upload Speed (Mbps)':[speed[2]],'Ping Speed (ms)':[speed[3]]})
    new_entry.to_csv("SpeedData.csv",index=False,mode='a',header=False)
    df = pd.read_csv("SpeedData.csv",index_col=False)
    return df


updatecsv(getspeed())