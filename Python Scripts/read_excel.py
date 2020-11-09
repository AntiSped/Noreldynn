import pandas as pd

sheet = pd.read_excel('Sources/Noreldynn_-_Stat_Calculators.xlsx', sheet_name=None)

for i in sheet.keys():
    print(i)

print("\n")
print(sheet["Player_Races"])
print(sheet["Player_Races"]["Oni"])

with open("test.txt", 'a') as file:
    for i in sheet.keys():
        file.write(str(sheet[i]))
