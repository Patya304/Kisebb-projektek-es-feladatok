'''
Az egész szám utolsó számjegye.
Kérjen be egy egész számot és írja ki az utolsó számjegyet
'''
szam = int(input("Adj meg egy számot: "))
utolso = szam % 10
print(f'Az egész szám utolsó számjegye {utolso}')
