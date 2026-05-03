# Exercise: Warm up - Weather Convertor
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
