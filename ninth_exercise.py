friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars = ['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' in friends)
print('John' in friends)

print(friends.union(my_friends))

print(friends.intersection(my_friends))

print(friends.difference(my_friends))

print(friends.symmetric_difference(my_friends))

cars_no_duplicates = list(set(cars))
print(cars_no_duplicates)