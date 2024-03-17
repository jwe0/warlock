import json

old = {}
new = {}



with open("sites.json") as f:
    config = json.load(f)
    for item, value in config.items():
        data = {

            "url" : value,
            "type" : "status-code",
            "check-value" : 200

        }
        new[item] = data


print(json.dumps(new, indent=4))