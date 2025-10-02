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

x = lambda x: x ** 2
print(x(8))

y =lambda parametro: parametro * (2 if parametro % 2 == 0 else 3)
print(y(7))

loop = lambda lista: sum(lista)
print(loop([1, 2, 3, 4, 5]))