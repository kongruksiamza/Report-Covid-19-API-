import requests 

#Case toDay
response=requests.get("https://covid19.th-stat.com/api/open/today")
data=response.json()
print("ติดเชื้อสะสม = ",data["Confirmed"])
print("หายแล้ว =",data["Recovered"])

#Case Summation
response=requests.get("https://covid19.th-stat.com/api/open/cases/sum")
data=response.json()
# print(data["Province"])

for i,(k,v) in enumerate(data["Province"].items()):
    print("Name = ",k ,"Case = ",v)