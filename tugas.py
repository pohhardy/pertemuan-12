data = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def in_number(x):
    if x < 10:
        return word[x]
    elif x >= 1_000_000_000:
        return in_number(x // 1_000_000_000) + ' billions ' + (in_number(x % 1_000_000_000) if x % 1_000_000 != 0 else '')
    elif x >= 1_000_000:
        return in_number(x // 1_000_000) + ' millions ' + (in_number(x % 1_000_000) if x % 1_000_000 != 0 else '')
    elif x >= 1_000:
        if x // 1_000 == 1:
            return " thousands " + (in_number(x % 1_000) if x % 1_000 != 0 else '')
        else:
            return in_number(x // 1_000) + " thousands " + (in_number(x % 1_000) if x % 1_000 != 0 else '')
    elif x >= 100:
        return in_number(x//100) + 'hundred' + in_number(x % 100)
    elif x >= 20:
        if x // 10 == 2:
            return 'twenty' + in_number(x % 10)
        elif x // 10 == 3:
            return 'thirty' + in_number(x % 10)
        elif x // 10 == 5:
            return 'fifty' + in_number(x % 10)
        else:
            return in_number(x // 10) + ('ty' if (x // 10) != 8 else 'y') + in_number(x % 10)
    else:
        if x == 10:
            return ' ten'
        elif x == 11:
            return ' eleven'
        elif x == 12:
            return ' twelve'
        elif x == 13:
            return ' thirteen '
        elif x == 14:
            return ' fourteen '
        elif x == 15:
            return ' fifteen'
        elif x == 16:
            return ' sixteen'
        elif x == 17:
            return ' seventeen'
        elif x == 18:
            return ' eighteen '
        elif x == 19:        
            return ' nineteen'

import os
while True:
    os.system('cls')
    try:
        x = int(input('angka ? '))
        print(f'{x:,} = {in_number(x)}')
    except:
        print('your input data is incorrect ...')
    os.system('pause')
