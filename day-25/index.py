# with open("day-25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
import pandas

# with open("day-25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur = data['Primary Fur Color']
grey_fur = data[fur == 'Gray']
cinnamon_fur = data[fur == 'Cinnamon']
black_fur = data[fur == 'Black']

black_fur_len = len(black_fur)
cinnamon_fur_len = len(cinnamon_fur)
grey_fur_len = len(grey_fur)

print(black_fur_len, cinnamon_fur_len, grey_fur_len)

print("-------------")