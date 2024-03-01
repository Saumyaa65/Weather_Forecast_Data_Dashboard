import requests

Api_key = "76cef3b4ac396f6a087e1736b621f0ea"


def get_data(place, days):
    url = (f"https://api.openweathermap.org/data/2.5/"
           f"forecast?q={place}&appid={Api_key}")
    response=requests.get(url)
    data=response.json()
    filtered_data= data['list'][:(8*days)]
    return filtered_data

if __name__=="__main__":
    print(get_data("Tokyo", 3))
