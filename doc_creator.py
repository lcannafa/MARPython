import json
import datetime as dt

now = str(dt.datetime.now())

with open('LOGS.json', "r") as logs:
    data = json.load(logs)

data['reporte'] = data['reporte'] + 1
data['fecha'] = now

with open('LOGS.json', "w") as f:
    json.dump(data, f, indent = 2)