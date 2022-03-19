# Funções map() e filter()
# Funções built-in que são usadas por esse tipo de estrutura de dados: map() e filter().
# A função map() é utilizada para aplicar uma determinada função em cada item de um objeto iterável.
#Tuplas: nas tuplas não é possível conseguimos fazer atribuições aposições específicas, uma vez que são objetos imutáveis.

# Exemplo map
print("Exemplo\n")
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")

print("\t------------\t")

# Exemplo tupla

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

print("\t------------\t")

# A função range() cria um objeto numérico iterável
numeros = list(range(0, 21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Números pares = {numeros_pares}")

numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
print(f"Números ímpares = {numeros_impares}")


