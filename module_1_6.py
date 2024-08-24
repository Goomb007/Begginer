my_dict = {'Sasha' : 2000, 'Sveta' : 2004, 'Dasha' : 1990}
print('Dict:', my_dict)
print('Existing value:', my_dict['Sasha'])
print('Not existing value:', my_dict.get('Denis'))
my_dict.update({'Pasha' : 1980,
                'Nastya' : 1993})
Sasha = my_dict.pop('Sasha')
print('Dleted value:', Sasha)
print('Modified dictionary:', my_dict)
print()
my_set = {1, 2, 3, 1, 2, 'Key', 'Home', 'Home', 'Key', (1, 2, 3)}
print('Set:', my_set)
my_set.update(['Hello', 'Kitty', 5])
my_set.discard('Key')
print('Modified set:', my_set)