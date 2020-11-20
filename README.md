# pertemuan-12
HARDY
pohhardy/tugas-pertemuan--12
data = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def in_number(x):
    if z < 10:
        return word[z]
    elif z >= 1_000_000_000:
        return in_number(z // 1_000_000_000) + ' billions ' + (in_number(z % 1_000_000_000) if z % 1_000_000 != 0 else '')
    elif z >= 1_000_000:
        return in_number(z // 1_000_000) + ' millions ' + (in_number(z % 1_000_000) if z % 1_000_000 != 0 else '')
    elif z >= 1_000:
        if z // 1_000 == 1:
            return " thousands " + (in_number(z % 1_000) if z % 1_000 != 0 else '')
        else:
            return in_number(z // 1_000) + " thousands " + (in_number(z % 1_000) if z % 1_000 != 0 else '')
    elif z >= 100:
        return in_number(z//100) + 'hundred' + in_number(z % 100)
    elif x >= 20:
        if z // 10 == 2:
            return 'twenty' + in_number(z % 10)
        elif z // 10 == 3:
            return 'thirty' + in_number(z % 10)
        elif z // 10 == 5:
            return 'fifty' + in_number(z % 10)
        else:
            return in_number(z // 10) + ('ty' if (z // 10) != 8 else 'y') + in_number(z % 10)
    else:
        if z == 10:
            return ' ten'
        elif z == 11:
            return ' eleven'
        elif z == 12:
            return ' twelve'
        elif z == 13:
            return ' thirteen '
        elif z == 14:
            return ' fourteen '
        elif z == 15:
            return ' fifteen'
        elif z == 16:
            return ' sixteen'
        elif z == 17:
            return ' seventeen'
        elif z == 18:
            return ' eighteen '
        elif z == 19:        
            return ' nineteen'

import os
while True:
    os.system('cls')
    try:
        z = int(input('angka ? '))
        print(f'{z:,} = {in_number(z)}')
    except:
        print('your input data is incorrect ...')
    os.system('pause')
