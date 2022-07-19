import csv
import math
mpower=-69
N=4
with open('Beacon_details.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ';')
    next(reader)
    details=[]
    for row in reader:
        detail={}
        detail['MAC Address']=row[0]
        detail['RSSI']=row[1]
        detail['Name']=row[3]
        details.append(detail)
details=details[1:]
#print(details)
rssi=[]
distance=[]
for x in details:
        x["distance (in m) "]=pow(10,((mpower -int(x['RSSI']))/(10 * N)))

for i in details:
    print(i)
