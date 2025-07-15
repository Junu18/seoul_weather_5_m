import requests # url : get요청
import csv      # csv로 저장
import os       # 폴더 생성
from datetime import datetime # 시간 변환

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
city= "seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
response = requests.get(url)
result = response.json()
temp = result["main"]["temp"] # 현재 기온
humidity = result["main"]["humidity"] # 현재 습도
main = result["weather"][0]["main"]
current_time = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
# 현재 기온

#csv
header = ["current_time","weather","temp","humidity"]

# 만약, seoul_weather.csv 없으면 만들고 !
# 있으면 덮어쓰기 >> 예외처리로 넣으면 되는거 아닌가?

csv_exist = os.path.exists("seoul_weather.csv")

with open("seoul_wather.csv","a") as file:
    writer = csv.writer(file)

    # csv가 한번도 안 만들어졌다면 , 헤더 추가!
    if not csv_exist: 
        writer.writerow(header)

    writer.writerow([current_time,main,temp,humidity])
    print("서울 기온 저장 완료")
    
