import json

purchases={}

with open(file='purchase_log.txt') as file:
    for line in file:
        purchases[json.loads(line).get("user_id")] = json.loads(line).get("category")