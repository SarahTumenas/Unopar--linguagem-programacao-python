# Set é um objeto do tipo set habilita operações matemáticas de conjuntos, tais como: união, intersecção, diferença, etc.
# Esse tipo de estrutura pode ser usado, portanto, em testes de associação e remoção de valores duplicados de uma sequência (PSF, 2020c).
# Não é possível criar um set vazio, com set = {}, pois essa é a forma de construção de um dicionário

# Objetos do tipo mapping são estruturas de dados que possuem um mapeamento entre uma chave e um valor são consideradas objetos do tipo mapping.
# Em Python, o objeto que possui essa propriedade é o dict (dicionário). Uma vez que esse objeto é mutável, conseguimos atribuir um novo valor a uma chave já existente.

# Criamos 4 exemplos de construção de objetos set.
vogais_1 = {'aeiou'} # sem uso do construtor
print(type(vogais_1), vogais_1)

vogais_2 = set('aeiouaaaaaa') # construtor com string
print(type(vogais_2), vogais_2)

vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
print(type(vogais_3), vogais_3)

vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
print(type(vogais_4), vogais_4)

# O construtor interpreta como um iterável e cria um conjunto em que cada caractere é um elemento, eliminando valores duplicados.
print(set('banana'))

print("\t------------\t")
# Exemplo 1 - Criação de dicionário vazio, com atribuição posterior de chave e valor
dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 30

print(dici_1)

print("\t------------\t")
# Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
dici_2 = {'nome': 'João', 'idade': 30}
print(dici_2)

print("\t------------\t")

# Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
dici_3 = dict([('nome', "João"), ('idade', 30)])
print(dici_3)

print("\t------------\t")
# Exemplo 4 - Criação de dicionário com a função built-in zip() e duas listas, uma com as chaves, outra com os valores.
dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))
print(dici_4)

print("\t------------\t")
#Testando se as diferentes construções resultam em objetos iguais.
print(dici_1 == dici_2 == dici_3 == dici_4)