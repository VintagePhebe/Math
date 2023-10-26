#this program is made for personal use and is not gonna be aimed to be productive or useful
import math
from math import *

kind_of_problem = input('si tratta di un problema riguardante:\n[1] piano inclinato\n[2] moto rettilineo uniforme\n[3] moto rettilineo uniformemente accellerato\n')

if kind_of_problem == '1':
    massa_iniziale = input('specificare la massa del corpo, se si conosce la forza peso scrivere forza peso N (es. 10N)\n')
    try:
        massa = float(massa_iniziale)
        F_peso = massa * 9.80665
    except:
        F_peso = float(massa_iniziale.replace('N', ''))

    angolo = input('l\'angolo è conosciuto?\n[no] se l\'angolo non è conosciuto\n[valore] specificare l\'angolo se esso è conosciuto\n')

    if angolo == 'no':
        h = float(input('specificare l\'altezza del piano inclinato\n'))
        l = float(input('specificare la lunghezza del piano inclinato\n'))

        F_parallela = (F_peso * h) / l
        print(f'la forza parallela vale: {round(F_parallela, 3)}N')
        F_perpendicolare_iniziale = F_peso ** 2 - F_parallela ** 2

        try:
            F_perpendicolare = math.sqrt(F_perpendicolare_iniziale)
            print(f'la forza perpendicolare vale: {round(F_perpendicolare, 3)}N')
        except:
            print('forza perpendicolare con valore immaginario')

    elif angolo.isdigit():
        try:
            angolo = int(angolo)
        except:
            pass


        F_parallela = F_peso * math.sin(math.radians(angolo))
        print(f'la forza parallela vale: {round(F_parallela, 3)}N')

        F_perpendicolare = F_peso * math.cos(math.radians(angolo))
        print(f'la forza perpendicolare vale: {round(F_perpendicolare, 3)}N')