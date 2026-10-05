km = float(input())
rashod = float(input())
cost = float(input())
gas = km / 100 * rashod
total_cost = gas * cost
print('Топливо:', gas, 'л')
print('Стоимость:', total_cost, 'руб')