woorden = []
counter = 0

while len(woorden) < 5:
    woord = input("Geef een woord: ")
    counter += 1
    
    if woord in woorden:
        print(f'Dit woord staat al in de lijst probeer een ander woord')
        woorden.remove(woord)
    else:
        print(f'Woord is toegevoegd: {woord}')
        woorden.append(woord)

for woord in woorden:
    print(woord)

print(f"Total woorden: {counter}")