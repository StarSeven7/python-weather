# Flask instance running on server
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) #make flask app


@app.route('/')    # def route access to web page
# / = homepage or also /index = homepage
@app.route('/index')
#def function and written something for route
def index():
    return render_template('index.html')

    
@app.route('/weather')

def get_weather():
    city = request.args.get('city')  # 'city' name come from url which inserted

    # Check for empty strings or string with only spaces
    # This step is not required here
    if not bool(city.strip()): #strip() remove spaces from begining & Ending
        city = "Kansas City"
    # code = 200 = Successful and 404 = Not found
    weather_data = get_current_weather(city) #weather_date come from API & if city name not available

    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html') # render_template is used to read 'html' file

    return render_template(
        "weather.html",
        title = weather_data["name"], 
        status = weather_data["weather"][0]["description"].capitalize(), 
        temp = f"{weather_data['main']['temp']:.1f}", 
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
