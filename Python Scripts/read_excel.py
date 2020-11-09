import pandas as pd
import math

sheet = pd.read_excel('Sources/Noreldynn_-_Stat_Calculators.xlsx', sheet_name=None)

# for i in sheet.keys():
    # print(i)

currentEP = input("Current Player EP : ")
currentEP = int(currentEP)

eptable = sheet["EP_Table"]

for row in eptable["Needed EP"].keys():
    row = int(row)
    if row != 125:
        if currentEP < math.floor(eptable["Needed EP"][row]):
            # print("Completed.")
            # print("{} is less than {}".format(currentEP, math.floor(eptable["Needed EP"][row])))
            print("The player is {} experience points away from Level {}".format(int(eptable["Needed EP"][row])-currentEP, eptable["Level"][row]))
            break
    else:
        if currentEP < eptable["Needed EP"][row]:
            print("Completed")


# for key in sheet["Player_Races"]["Oni"].keys():
    # print("{} >> {}".format(sheet["Player_Races"]["Stats"][key], sheet["Player_Races"]["Oni"][key]))
