import json
from database import clientes

object_json = json.dumps(clientes, indent=4)

with open("dashboard.json", "w") as file:
    file.write(object_json)
