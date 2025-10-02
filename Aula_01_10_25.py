a = [5, 10, 15, 20, 25]

def soma(lista: list) -> int:
    res = 0
    for i in lista:
        res += i

    return res

def somar(lista: list, i: int) -> int:
    return lista[i] + somar(lista, i + 1)

r = soma(a)
print(r)

soma = lambda a, b: a + b
print(soma(3, 5))