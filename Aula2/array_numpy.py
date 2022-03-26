nomes = 'João Marcela Sonia Daryl Vernon Eder Mechelle Edan Igor Ethan Reed Travis Hoyt'.split()

print('Marcela' in nomes)
print('Roberto' in nomes)

# Criando várias formas de matrizes com a biblioteca NumPy.

import numpy
# Cria matriz 1 linha e 1 coluna
matriz_1_1 = numpy.array([1, 2, 3])

# Cria matriz 2 linhas e 2 colunas
matriz_2_2 = numpy.array([[1, 2], [3, 4]])

#Cria matriz 3 linhas e 2 colunas
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) #

#Cria matriz 2 linhas e 3 colunas
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]])

print(type(matriz_1_1))
print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_3_2 = \n', matriz_3_2)
print('\n matriz_2_3 = \n', matriz_2_3)