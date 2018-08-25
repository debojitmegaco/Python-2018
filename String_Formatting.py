#String Formatting in Python

name = 'Paul'
age = 23
Location = 'India'

print("Mr. %s is being aged %d is from %s" % (name, age, Location))
print("Mr. {} is being aged {} is from {}".format(name, age, Location))
print(f'Mr. {name} is being aged {age} is from {Location}')

student = {'name': 'Paul', 'age': 23, 'Location': 'India'}
print("Mr. {name} is being aged {age} is from {Location}".format(**student))

Teachers = ['John','Kevin','Tarus']
print("Mr. {2}, {1} and {0} are new teachers in Class".format(*Teachers))



	