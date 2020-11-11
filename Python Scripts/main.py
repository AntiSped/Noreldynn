import json
import ast
import pandas as pd

sheet = pd.read_excel('Sources/Noreldynn_-_Stat_Calculators.xlsx', sheet_name=None)
keys = sheet["Player_Races"].keys()


for key in keys:
    with open("Sources/{}_data.json".format(key), 'r') as file:
        print(sheet["Player_Races"][key])
        data = json.dumps(ast.literal_eval(file.read()), sort_keys=True, indent=4, default=str)
        print(data)
        with open("Sources/{}_data.json".format(key), 'w') as file:
            file.write(str(data))