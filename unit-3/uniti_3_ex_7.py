people = ['one','two','three']
message = '我想和你一起吃饭'
no_message = '不能来吃饭'

people.pop()
people.append('baba')
people.insert(0,'mama')
people.insert(3,'meimei')
people.append('jiejie')
sorry_message = '对不起，我只能和两个人吃饭'
print(people)
print(sorry_message)
people_jiejie = people.pop()
print(sorry_message + ',' + people_jiejie)
people_baba = people.pop()
print(sorry_message + ',' + people_baba)
people_meimei = people.pop()
print(sorry_message + ',' + people_meimei)
people_two = people.pop()
print(sorry_message + ',' + people_two)
lai_message = '你们可以来'
print(lai_message + ',' + people[0])
print(lai_message + ',' + people[1])
del people[0]
del people[1]
print(people)