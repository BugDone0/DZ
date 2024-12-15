import json

purchases={}

with open(file='purchase_log.txt') as file:
    for line in file:
        purchases[json.loads(line).get("user_id")] = json.loads(line).get("category")

f_funnel = open('funnel.csv', 'w')
visit_log = open('visit_log.csv', 'r')
for line in visit_log:
    user_inf=line.split(',')
    try:
        f_funnel.write(f"{user_inf[0]}, {user_inf[1].strip()}, {purchases[user_inf[0]]}\n")
    finally:
        continue

visit_log.close()
f_funnel.close()
