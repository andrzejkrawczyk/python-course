sum() / float(len())

a = len(collection)
if a % 2:
    pass
    collection[a / 2]
else:
    pass


import csv
import pprint
from collections import defaultdict

reader = None
rows = []
with open('some_data.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

    #print(rows)


def list_of_unique_elements(rows, attribute):
    result = []
    for index, row in enumerate(rows):
        car_maker = row[attribute]
        if car_maker not in result:
            result.append(row[attribute])

    return result

#gender
#Female
#Male
females = 0
males = 0

distribution = {
    "year": defaultdict(int),
    "car_model": defaultdict(int),
    "car_producer": defaultdict(int)
}
for row in rows:
    year = row["car_model_year"]
    car_model = row["car_model"]
    car_producer = row["car_make"]

    distribution["year"][year] += 1
    distribution["car_model"][car_model] += 1
    distribution["car_producer"][car_producer] += 1

a = pprint.pformat(distribution["year"], indent=4)
pprint.pprint(a)
a = pprint.pformat(distribution["car_model"], indent=4)
print(a)
a = pprint.pformat(distribution["car_producer"], indent=4)
print(a)


#print(list_of_unique_elements(rows, "car_make"))
#print(list_of_unique_elements(rows, "car_model_year"))
#print(list_of_unique_elements(rows, "car_model"))

#typy_samochodow = set([ row["car_make"] for row in rows ])
#typy_samochodow = { row["car_make"] for row in rows }
# print(result)
# print(len(result))

# for i, e in enumerate(range(100, 130, 1)):
#     print(i, e)