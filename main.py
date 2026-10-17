import re
def razbor(stroka):
    return re.findall(r'\d+\.?\d*|[a-zA-Z]+|[()+\-*/>,;]', stroka)

def slozhenie(spisok):
    global i
    chislo = umn(spisok)

    while i < len(spisok) and spisok[i] in ['+', '-']:
        znak = spisok[i]
        i += 1
        sec = umn(spisok)

        if znak == '+':
            chislo += sec
        else:
            chislo -= sec

    return chislo


def umn(spisok):
    global i
    chislo = chast(spisok)

    while i < len(spisok) and spisok[i] in ['*', '/']:
        znak = spisok[i]
        i += 1
        sec = chast(spisok)

        if znak == '*':
            chislo *= sec
        else:
            chislo /= sec

    return chislo


def chast(spisok):
    global i

    znak = spisok[i]

    if znak == '-':
        i += 1
        return -chast(spisok)

    if znak == '+':
        i += 1
        return chast(spisok)

    if znak == '(':
        i += 1
        chislo = sravnenie(spisok)
        if i >= len(spisok) or spisok[i] != ')':
            raise ValueError('Незакрытая скобка')
        i += 1
        return chislo

    if znak == 'max':
        i += 2
        chisla = [slozhenie(spisok)]

        while i < len(spisok) and (spisok[i] == ',' or spisok[i] == ';'):
            i += 1
            chisla.append(slozhenie(spisok))

        i += 1
        return max(chisla)

    i += 1
    return float(znak)


def sravnenie(spisok):
    global i
    chislo = slozhenie(spisok)

    if i < len(spisok) and spisok[i] == '>':
        i += 1
        sec = slozhenie(spisok)
        return chislo > sec

    return chislo

print('Для выхода введите "exit"')
while True:
    stroka = input("Введите выражение: ")
    if stroka == 'exit' or stroka == 'EXIT':
        break
    spisok = razbor(stroka)
    i = 0
    try:
        print("Результат:", sravnenie(spisok))
    except:
        print("Ошибка")
