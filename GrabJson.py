import json
import requests
from datetime import timedelta
import datetime 
from datetime import timedelta
from timeit import default_timer

# data = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35
# }

def func(requestLink):    
    response = requests.post(requestLink,headers = header)
    data = json.loads(response.text)
    data["metaData"]["cd"] = str(_currentDate)

    f.write("\n,\n")
    # print(data)
    json.dump(data, f)

header = {
"content-encoding": "gzip",
"content-type": "application/json",
"date": "Thu, 01 May 2019 19:30:28 GMT",
"server": "hello",
"status": "200",
"strict-transport-security": "max-age=31536000",
"vary": "Accept-Encoding",
"x-content-type-options": "nosniff",
"x-frame-options": "SAMEORIGIN",
"x-xss-protection": "1",
}

start_time = default_timer()
_currentDate = datetime.datetime.today()
path = r"C:\Users\Rajesh\Desktop\Data.json"

with open(path, "a") as f:  
    for i in range(30):
        date = (_currentDate + timedelta(days = i)).strftime("%d-%b-%y")
        func("https://www.redbus.in/search/SearchResults?fromCity=123&toCity=122&src=Chennai%20(All%20Locations)&dst=Bengaluru&DOJ=" + str(date) + "&sectionId=0&groupId=0&limit=0&offset=0&sort=0&sortOrder=0&meta=true&returnSearch=0")
        func("https://www.redbus.in/search/SearchResults?fromCity=122&toCity=123&src=Bengaluru&dst=Chennai%20(All%20Locations)&DOJ=" + str(date) + "&sectionId=0&groupId=0&limit=0&offset=0&sort=0&sortOrder=0&meta=true&returnSearch=0")
        print(i+1)

end_time = default_timer()                
print(end_time - start_time)
