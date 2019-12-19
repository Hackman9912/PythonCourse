# dictionary comprehenison

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
secrets = ['Batman', 'Superman', 'Spidermand', 'Wolverine', 'Deadpool']
# I want a dict('name', 'secret') for each name, secret in the zip(names, secrets)
# without dict comprehension

my_dict = {}
for name, secret in zip(names, secrets):
    my_dict[name] = secret
print(my_dict)

# with dict comprehension
my_dict2 = {name:secret for name, secret in zip(names, secrets)}
print(my_dict2)
