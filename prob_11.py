n = int(input("Dati numarul de elemente: "))
if 0 < n < 10:
    lst = []
    for i in range(n):
        i = int(input("Introduceti un numar: "))
        lst.append(i)
    print('a) afişează pe ecran componentele tabloului la un interval de 5 poziţii\n', lst[::5])
    print('b) afişează pe ecran numerele în ordinea inversă a introducerii în calculator\n', lst[::-1])
    print('c) sortează componentele tabloului în ordine descrescătoare\n', sorted(lst, reverse=True))
    pare = list(filter(lambda x: (x % 2 == 0) , lst))
    impare = list(filter(lambda x: (x % 2 != 0) , lst))
    print('d) afişează pe ecran doar componentele pare\n', pare)
    print('e) afişează pe ecran media aritmetică a componentelor pare\n', sum(pare) / len(pare))
    print('f) afişează pe ecran doar componentele impare\n', impare)
    x = int(input("Dati numarul de minim: "))
    y = int(input("Dati numarul la care se divide: "))
    num = list(filter(lambda i: (i > x) and (i % y != 0), lst))
    print(f'g) afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură)\n ', num)
    x = int(input("Dati numarul minim: "))
    y = int(input("Dati numarul maxim: "))
    print(f'h) afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură)\n', [i for i in lst if (i > x) and (i < y)])
    m = list(filter(lambda i: (i % 2 != 0) and (i < 0), lst))
    n = []
    for i in m:
        n.append(lst.index(i))
    print(f'i) afişează pe ecran poziţiile (indicii) componentelor impare negative\n {n}')
    m = list(filter(lambda i: ((i > 9) and (i < 100)) or ((i < -9) and (i > -100)), lst))
    n = []
    for i in m:
        n.append(lst.index(i))
    print(f'j) afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative\n {n}')
    k = lst.copy()
    k[0] = min(lst)
    print(f'k) Inlocueste prima componenta a tabloului cu valoare minima din tabloul respectiv:\n {k}')
    l = lst.copy()
    l[l.index(min(l))] = lst[0]
    print(f'l) Inlocueste componenta cu valoare minima din tabloul respectiv cu prima valoare a tabloului:\n {l}')
    nr_pare = list(filter(lambda x: (x % 2 == 0) , lst))
    print(f'm) Creeaza un tablou format din componentele pare ale tabloului introdus de la tastatura:\n {nr_pare}')
    div_3 = list(filter(lambda x: (x % 3 == 0) , lst))
    print(f'n) Creeaza un tablou format din componentele divizibile cu 3 ale tabloului introdus de la tastatura:\n {div_3}')
    ls = []
    for i in lst:
        divizori = []
        for j in range (1, i + 1):
            if i % j == 0:
                divizori.append(j)
        for j in range (i - 1, 0):
            if i % j == 0:
                divizori.append(j)
                if j < 0:
                    divizori.append(-j)
        print(divizori)
        if 1 <= len(divizori) <= 4:
            ls.append(i)
    print(f'o) creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori\n {ls}')
else:
    print("Dati numarul de elemente mai mic de 10 si mai mare ca 0")