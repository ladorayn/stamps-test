import requests
from datetime import datetime

apikey = "4224b0397f16c439ea22cb019a15d92f"
city = "Jakarta"

def apa_bole_app():
  for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Apa"
    if i % 5 == 0:
        output += "Bole"
    if not output:
        output = str(i)
    print(output, end="")
    if i != 100:
        print(", ", end="")
  
def WeatherAPI_app():
  dates = []
  print("Weather Forecast:")
  
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric&limit=1"

  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()

    if "list" in data:
      forecasts = data["list"]
      for forecast in forecasts:
          date = forecast["dt_txt"].split()[0]
          if date not in dates:
            dates.append(date)
            temperature = forecast["main"]["temp"]
            
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            day_name = date_obj.strftime("%A")
            day = date_obj.strftime("%d")
            month_name = date_obj.strftime("%B")
            year = date_obj.strftime("%Y")
            formatted_date = f"{day_name[0:3]}, {day} {month_name[0:3]} {year}"

            print(f"{formatted_date}: {temperature}°C")
    else:
        print("No forecast data available.")
  else:
      print("Error:", response.status_code)  


while(1):
  print("========= Mini Test STAMPS =========")
  print()
  print("Choose Problem")
  print("1. ApaBole Problem")
  print("2. WeatherAPI Problem")

  try:
    problem = eval(input("Pick the number [1/2]\n"))
  except:
    continue

  if problem == 1:
    apa_bole_app()
    print()
    print()
  elif problem == 2:
    WeatherAPI_app()
    print()
    print()
  else:
    continue

  cont = str(input("Continue app? [y/n or any key]\n"))

  if cont == "y":
    continue
  elif cont == "n":
    break
  else:
    break


