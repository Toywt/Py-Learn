motorcycles = ['yamaha','halei','hongqi']
# print(motorcycles)
motorcycles[0] = 'yiqi'
# print(motorcycles)

motorcycles.append('dazhong')
# print(motorcycles)

motorcycles.insert(1,'changan')
# print(motorcycles)

del motorcycles[0]

# print(motorcycles)

# last_moto = motorcycles.pop()
# print(motorcycles)
# print(last_moto)
# frist_moto = motorcycles.pop(0)
# print(motorcycles)
# print(frist_moto)
halei_moto = motorcycles.remove('halei')
print(motorcycles)
print(halei_moto)