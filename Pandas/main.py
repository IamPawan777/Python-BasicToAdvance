# with open("Pandas/weather.csv", "r") as f:
#     fil = f.readlines()
#     print(fil)



# import csv
# with open('Pandas/weather.csv') as f:
#     data = csv.reader(f)
#     tempList = []
#     for i in data:
#         if i[1] != 'temp':
#             print(i[1])





import pandas as pd
data = pd.read_csv('Pandas/weather.csv')
# print(data)
# print(data.head(2))
# print(data.temp)                  # column
print(data[data.temp == 9])         # row
