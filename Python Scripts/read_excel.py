import pandas as pd
import math
import json
import ast
import os

try:
    sheet = pd.read_excel('Sources/Noreldynn_-_Stat_Calculators.xlsx', sheet_name=None)
    not_a_number = float("nan")

    def keys():
        for i in sheet.keys():
            print(i)

    def deep_keys():
        for i in sheet["Player_Races"].keys():
            print(i)
            #test

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
        
        keys = keys.delete(0)

        print(keys)
        

        for race in keys:
            print(race)
            print(sheet["Player_Races"][race])

            dict = {}
            for key in sheet["Player_Races"][race].keys():
                dict[sheet["Player_Races"]["Stats"][key]] = sheet["Player_Races"][race][key]
            
            with open("{}_data.json".format(race), 'w') as file:
                file.write(json.dumps(ast.literal_eval(str(dict)), sort_keys=True, indent=4))

    def refresh_excel():
        sheet = pd.read_excel('Sources/Noreldynn_-_Stat_Calculators.xlsx', sheet_name=None)
        keys = sheet["Player Races"].keys()

        keys = keys.delete(0)


        for race_key in keys:
            dict = {}
            for col_key in sheet["Player Races"][race_key].keys():
                if pd.isnull(sheet["Player Races"][race_key][col_key]):
                    dict[sheet["Player Races"]["Stats"][col_key]] = "Not a Number"
                else:
                    dict[sheet["Player Races"]["Stats"][col_key]] = sheet["Player Races"][race_key][col_key]
                with open("Sources/{}_data.json".format(race_key), 'w') as file:
                    data = json.dumps(dict, sort_keys=True, indent=4, default=str)
                    file.write("")
                    file.write(str(data))
        print("Completed file refresh.")

    def start():
        rsp = input("Keys / Experience Table / Oni Information / Type Script / Deep Keys / Refresh >> ")
        if rsp == "keys" or rsp == "Keys":
            keys()
        elif rsp == "experience table" or rsp == "Experience table" or rsp == "Experience Table":
            exp_table()
        elif rsp == "oni information" or rsp == "Oni information" or rsp == "Oni Information":
            oni_information()
        elif rsp == "type script":
            type_script()
        elif rsp == "deep keys" or rsp == "Deep keys" or rsp == "Deep Keys":
            deep_keys()
        elif rsp == "test" or rsp == "Test":
            test()
        elif rsp == "refresh" or rsp == "refresh excel" or rsp == "Refresh" or rsp == "Refresh Excel":
            refresh_excel()
        else:
            raise Exception("Failed to determine what task to complete.")

    start()
except KeyboardInterrupt:
    os.system('clear || cls')
    print("The program has been closed forcefully.")
