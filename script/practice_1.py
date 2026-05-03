# Exercise 1: Warm up - Weather Convertor
def celsius_to_fahrenheit(temp_c):
    temp_f = temp_c * 1.8 + 32
    return temp_f

def describe_weather(temp_c, unit="C"):
    if unit == "C":
        if temp_c <= 0 :
            return "Freezing"
        elif 0 < temp_c < 15:
            return "Cold"
        elif 15 <= temp_c < 25:
            return "Comfortable"
        elif temp_c >= 25:
            return "Hot"
    elif unit == "F":
        temp_c = (temp_c - 32) * 5 / 9
        return describe_weather(temp_c, unit ="C")
        # advanced version
        # return describe_weather((temp_c - 32) * 5 / 9)

# ── Tests ──
assert celsius_to_fahrenheit(0) == 32.0
assert celsius_to_fahrenheit(100) == 212.0
assert describe_weather(-5) == "Freezing"
assert describe_weather(10) == "Cold"
assert describe_weather(20) == "Comfortable"
assert describe_weather(30) == "Hot"
assert describe_weather(86, unit="F") == "Hot"
assert describe_weather(32, unit="F") == "Freezing"
print("✅ PASS — Solid foundation!")


# Exercise 2: Weather Dictionary
def get_weather_summary(data):
    template = "{city}: {temperature}°C, {condition} (humidity: {humidity}%, wind: {wind_speed} km/h)"
    return template.format_map(data)

def is_good_weather(data):
    weather_summary = get_weather_summary(data)

# ── Tests ──
sample = {"city": "Prague", "temperature": 18, "humidity": 65,
          "wind_speed": 12, "condition": "cloudy"}

rainy = {"city": "Brno", "temperature": 16, "humidity": 90,
         "wind_speed": 25, "condition": "rainy"}

hot = {"city": "Ostrava", "temperature": 32, "humidity": 55,
       "wind_speed": 8, "condition": "sunny"}

assert get_weather_summary(sample) == "Prague: 18°C, cloudy (humidity: 65%, wind: 12 km/h)"
assert is_good_weather(sample) == True, "Prague should be good weather"
assert is_good_weather(rainy) == False, "Rainy+humid+windy should be False"
assert is_good_weather(hot) == False, "Too hot should be False"
print("✅ PASS — Dictionary access mastered! This is exactly how API data looks.")
# print(get_weather_summary(sample))