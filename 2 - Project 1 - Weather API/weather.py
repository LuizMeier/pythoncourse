import requests

# api_key = ""

# lat = -25.4278
# lon = -49.2731

# try:
#     #response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}")
#     response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
# except:
#     print("An error occurred")

# response_json = response.json()

# time = response_json["current"]["time"]
# temperature = response_json["current"]["temperature_2m"]


# print(f"In Curitiba it is currently {temperature} degrees")


class City:
    def __init__(self, name, lat, lon, wind_speed):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
        except:
            print("An error occurred")

        self.response_json = response.json()

        self.time = self.response_json["current"]["time"]
        self.temperature = self.response_json["current"]["temperature_2m"]

    def temp_print(self):
        print(f"In {self.name} it is currently {self.temperature} degrees")


my_city = City("Curitiba", -25.4278, -49.2731)
my_city.temp_print()

vacation_city = City("Portland", 45.5051, -122.6750)
vacation_city.temp_print()
print(vacation_city.response_json["current"])