file = open('../cities.csv', 'r')
cities = []
for city in file:
    cities.append(city.strip().split(',')[0])
file.close()
print(cities)
