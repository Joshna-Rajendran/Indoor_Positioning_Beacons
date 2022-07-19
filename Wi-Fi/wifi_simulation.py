import subprocess
import re
import math
import sched, time
s = sched.scheduler(time.time, time.sleep)
txpower = -40
#print(command_output)
def refreshing_wifi(sc):
    command_output = subprocess.run(["netsh", "wlan", "show", "network","mode=Bssid"], capture_output = True).stdout.decode()
    profile_names = (re.findall("^SSID (.*)\r", command_output,re.MULTILINE))
    wifi_list = []
    ssid_list=[]
    for i in range(len(profile_names)):
        ssid_list.append(command_output.split("Network type"))
    ssid_list[0].pop(0)
    #print(ssid_list)
    if len(profile_names) != 0:
        j=0
        for name in profile_names:
            wifi_profile = {}
            wifi_profile["ssid"] = name.split(":")[1].strip()     
            signals=(re.findall("Signal(.*)\r",str(ssid_list[0][j]),re.MULTILINE))
            #print(signals)
            wifi_profile["signal"]=[]
            for i in signals:
                wifi_profile["signal"].append(i.strip().split(":")[1].split("%")[0])
            wifi_list.append(wifi_profile)
            j=j+1


    max_signals=[]
    rssi=[]
    distance=[]
    for x in wifi_list:
        x["maxsignal"]=int(max(x["signal"]))
        if(x["maxsignal"] <= 0) :
            x["rssi"] = -100
        elif(x["maxsignal"]>= 100):
            x["rssi"] = -50
        else:
            x["rssi"] = (x["maxsignal"] / 2) - 100
        ratio =(txpower-x["rssi"])/40
        x["distance"]= round(math.pow(10,ratio),4)-1

    for i in wifi_list:
        print(i)
    sc.enter(10, 1, refreshing_wifi, (sc,))
    print("------------------------------------------------------------------------------------------")

s.enter(10, 1, refreshing_wifi, (s,))
s.run()
