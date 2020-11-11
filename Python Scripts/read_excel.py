import pandas as pd
import math

sheet = pd.read_excel('Sources/Noreldynn_-_Stat_Calculators.xlsx', sheet_name=None)

def keys():
    for i in sheet.keys():
        print(i)

def deep_keys():
    for i in sheet["Player_Races"].keys():
        print(i)

def exp_table():
    currentEP = input("Current Player EP : ")
    currentEP = int(currentEP)

    eptable = sheet["EP_Table"]

    for row in eptable["Needed EP"].keys():
        row = int(row)
        if row != 125:
            if currentEP < math.floor(eptable["Needed EP"][row]):
                print("The player is {} experience points away from Level {}".format(int(eptable["Needed EP"][row])-currentEP, eptable["Level"][row]))
                break
        else:
            if currentEP < eptable["Needed EP"][row]:
                print("Completed")

def oni_information():
    for key in sheet["Player_Races"]["Oni"].keys():
        print("{} >> {}".format(sheet["Player_Races"]["Stats"][key], sheet["Player_Races"]["Oni"][key]))

def test():
    keys = sheet["Player_Races"]["Stats"].keys()

    print(keys.stop)

def type_script():
    keys = sheet["Player_Races"].keys()

    print(keys)
 
    for race in sheet["Player_Races"].keys():
        print(race)
        print(sheet["Player_Races"][race])

        dict = {}
        for key in sheet["Player_Races"][race].keys():
            dict[sheet["Player_Races"]["Stats"][key]] = sheet["Player_Races"][race][key]
        
        with open("{}_data.json".format(race), 'a') as file:
            file.write(str(dict))

def start():
    rsp = input("Keys / Experience Table / Oni Information / Type Script / Deep Keys >> ")
    if rsp == "keys" or rsp == "Keys":
        keys()
    elif rsp == "experience table" or rsp == "Experience table" or rsp == "Experience Table":
        exp_table()
    elif rsp == "oni information" or rsp == "Oni information" or rsp == "Oni Information":
        oni_information()
    elif rsp == "type script":
        type_script()
    elif rsp == "deep keys":
        deep_keys()
    elif rsp == "test":
        test()
    else:
        raise Exception("Failed to determine what task to complete.")

start()
