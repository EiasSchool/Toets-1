naam = input('Wat is je naam?\n')
leeftijd = int(input('Hoe oud ben jij?\n'))

if leeftijd >= 18:
    print(f'Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).')
else:
    print(f'Beste {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in :-( ')