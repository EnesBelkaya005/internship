names1 = ['john ClEEse','Eric IDLE','michael']
names2 = ['graHam chapman', 'TERRY', 'terry jones']
text = 'You are invited to the party on saturday.'
names1 += names2
for index in range(2):
    names1.append(input('Enter a new name: '))

for name in names1:
    text1 = name.title() + '! ' + text
    print(text1)