total_rain = 0.0
total_wind = 0.0
count = 0

line = input()

while line != "-1.0":
    rain, wind = map(float, line.split())
    total_rain += rain
    total_wind += wind
    count += 1
    line = input()

average_rain = total_rain / count
average_wind = total_wind / count
severity = (average_rain * 10) + average_wind

print("The average rain is", round(average_rain, 1), "inches")
print()
print("The average wind is", round(average_wind, 1), "mph")
print()
print("The weather severity for these", count, "readings is:", round(severity, 1))