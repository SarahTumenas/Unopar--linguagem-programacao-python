#Objetos do tipo sequência

# Sequência de caracteres
texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")

# Por meio da estrutura de repetição, imprimimos cada elemento da lista juntamente com seu índice.
vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')

# função split(), usada para "cortar" um texto e transformá-lo em uma lista. Essa função pode ser usada sem nenhum parâmetro: texto.split().
# Nesse caso, a string será cortada a cada espaço em branco que for encontrado.
# Caso seja passado um parâmetro:texto.split(","), então o corte será feito no parâmetro especificado.
texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")

