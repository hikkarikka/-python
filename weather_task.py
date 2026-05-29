import requests

base_url= "https://api.openweathermap.org/data/2.5/weather"
api_key = "d8cbd802ab778feace8c7ae678fae712"

def menu():
    print("1.узнать погоду")
    print("0. Выйти")

def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lamg": "ru"
    }
    try:
        response = requests.get(base_url,params=params)
        response.raise_for_status
        data = response.json
        
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "wind" : data["wind"]["speed"]

        }
        
        print(data)


    except requests.exceptions.RequestException as e:
        print(f'ошибка GET: {e}')


def main():
    while True:
        menu()
        choice = input("выбрать действие:")

        if choice =="1":
            city = input("")
            weather = get_weather(city)
            print(f":{city}")
            print(f'{weather["temperature"]}')
            print(f':{weather["feel_like"]}')
            print(f':{weather["wind"]}')

        elif choice == "0":
            break

        else:
            print("")


if __name__ == "__main__":
    main()