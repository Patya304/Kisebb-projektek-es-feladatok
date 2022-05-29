'''
Két számjegy
Kérjen be egy kétjegyű számot és  nyomtassa ki a számjegyeit külön-külön.
Például ha a beadott szám 17, akkor a kiírás:
1 7
'''
szam = int(input("Adj egy kétjegyű számot: "))
print('Az általad megadott 2jegyű szám külön-külön:', szam//10, szam%10)
