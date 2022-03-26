# Busca linear (ou Busca Sequencial)
# Percorre os elementos da sequência procurando aquele de destino, começa por uma das extremidades da sequência e vai percorrendo até encontrar (ou não) o valordesejado.
# Pesquisa linear examina todos os elementos da sequência até encontrar o de destino, o que pode ser muito custoso computacionalmente.


def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento: return True
    return False

import random

lista = random.sample(range(100), 20)
print(sorted(lista))
executar_busca_linear(lista,10)






vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)
