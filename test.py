#!/usr/bin/env python
print('hello world')
ingredients = ''
while ingredients != 'quit':
	ingredients = input("Choose pizza ingredients: ")
	message = str(ingredients) + ' OK!'
	print(message)
print('OK!')

flag1 = 1
while flag1:
	age = input('How old are you: ')
	if age != 'quit':
		age = int(age)
		if age < 3:
			print('free')
		elif age >= 3 and age < 12:
			print('10')
		else:
			print('15')
	else:
		flag1 = 0
print('thank you')


while 1:
	age = input('How old are you: ')
	if age != 'quit':
		age = int(age)
		if age < 3:
			print('free')
		elif age >= 3 and age < 12:
			print('10')
		else:
			print('15')
	else:
		break
