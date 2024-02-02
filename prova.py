subcadena = list()


def joinstr(subcadena):
    string = ""
    for x, val in enumerate(subcadena):
        if x == len(subcadena) - 1:
            string += val
        else:
            string += val + " "
    return string


def split(vocales):
    Vectorpalabras = []
    tmp = ''
    for c in vocales:
        if c == ' ':
            if tmp != '':
                Vectorpalabras.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        Vectorpalabras.append(tmp)

    return Vectorpalabras


cadena = str(input("Ingrese una cadena: "))
vocales = 'a e i o u'
vocales = split(vocales)
temp = dict(zip(vocales, vocales[1:] + [vocales[0]]))
subcadena = ([temp.get(ele, ele) for ele in cadena])
subcadena = joinstr(subcadena)
print("La nueva cadena es: " + str(subcadena))