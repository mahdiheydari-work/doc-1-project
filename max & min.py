import json

with open('data.json', 'r') as file:
    data_dict = json.load(file)

data = []
for item in data_dict["data"]:
    try:
        data.append(int(item))
    except (ValueError, TypeError):
        print(f"Skipping invalid value: {item}")

# data = [4,112,12,41,56,222,3245,213,534,6455,7434,1212,1121,1111,2233]

max = 0
min = 100000000

for i in (data):
    if i < min:
        min = i
    if i > max:
        max = i
print (min)
print (max)


