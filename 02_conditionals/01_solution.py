age = 4
species = 'Cat'

if age <= 2 and species == 'Dog':
    print('Puppy food')
elif age > 5 and species == 'Cat':
    print('Senior cat food')
elif age <= 5 and species == 'Cat':
    print('Junior cat food')
else:
    print('Invalid')
