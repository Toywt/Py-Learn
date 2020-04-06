people = ['one','two','three']
message = '我想和你一起吃饭'
no_message = '不能来吃饭'

print(no_message + ',' + people[2])
people.pop()
people.append('baba')
people.insert(0,'mama')
people.insert(3,'meimei')
people.append('jiejie')
print(message + ',' + people[0])
print(message + ',' + people[1])
print(message + ',' + people[2])
print(message + ',' + people[4])
print(message + ',' + people[5])
print(message + ',' + people[6])