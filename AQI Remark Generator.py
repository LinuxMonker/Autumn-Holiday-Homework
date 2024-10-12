print("AQI Remark Generator")

def aqi_remark(aqi):
    if 0 <= aqi <= 50:
        return "Good"
    elif 51 <= aqi <= 100:
        return "Satisfactory"
    elif 101 <= aqi <= 200:
        return "Moderate"
    elif 201 <= aqi <= 300:
        return "Poor"
    elif 301 <= aqi <= 400:
        return "Very Poor"
    elif 401 <= aqi <= 500:
        return "Severe"
    else:
        return "Invalid AQI"

city = input("Enter your city name: \n")
aqi = int(input(f"Enter the AQI for {city}: \n"))
remark = aqi_remark(aqi)

print(f"City: {city}")
print(f"AQI: {aqi}")
print(f"Remark: {remark}")
