# from dotenv import load_dotenv # Load environment variables from a .env file into your application's environment.
# from pprint import pprint 
# import requests #get data from url
# import os   # Access the variables

# # load_dotenv(): Loads the environment variables from the .env file.
# # os.getenv(): Reads the environment variables using os.environ to access the values.



# # Load environment variables from the .env file
# load_dotenv()

# def get_current_weather(city="Hyderabad"):

#     request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

#     weather_date = requests.get(request_url)
#     return weather_date

# if __name__ == "__main__":
#     print("\n *** Welcome to Current Weather Condition \n\n")
#     city = input("\nEnter the city name : ")
#     weather_date = get_current_weather(city)

#     pprint(weather_date)

################ DOVE #########################
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Kansas City"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    # This step is not required here
    if not bool(city.strip()): #strip() remove spaces from begining & Ending
        city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)