#Estrutura condicional simples:
a = 5
b = 10
if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)

#Estrutura composta:
a = 10
b = 5
if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)
else:
    print("a é maior do que b")
    r = a - b
    print(r)

#Estrutura encadeada, devemos usar o comando "elif", que é uma abreviação de else if.
codigo_compra = 5111
if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")

#Estrutura condicional usando os operadores booleanos. Um aluno só pode ser aprovado caso ele tenha menos de 5 faltas
# e média final igual ou superior a 7.
qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")


#Assim como as operações matemáticas possuem ordem de precedência, as operações booleanas também têm. Essa prioridade obedece à seguinte ordem: not primeiro, and em seguida e or por último (BANIN, 2018).

A = 15
B = 9
C = 9
print(B == C or A < B and A < C)
print((B == C or A < B) and A < C)


#O comando while deve ser utilizado para construir e controlar a estrutura decisão, sempre que o número de repetições não seja conhecido.

numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")

#o comando "for" seguido da variável de controle "c", na sequência o comando "in", por fim, a sequência sobre a qual a estrutura deve iterar.
# Os dois pontos marcam o início do bloco que deve ser repetido.

nome = "Guido"
for c in nome:
    print(c)

#Com o comando for, podemos usar a função enumerate() para retornar à posição de cada item, dentro da sequência. Considerando o exemplo dado,
# no qual atribuímos a variável "nome" o valor de "Guido", "G" ocupa a posição 0 na sequência, "u" ocupa a posição 1, "i" a posição 2,
# e assim por diante. Veja que a variável "i" é usada para capturar a posição e a variável "c" cada caractere da palavra.

nome = "Guido"
for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")

#A função range() pode ser usada de três formas distintas:
# Método 1: passando um único argumento que representa a quantidade de vezes que o laço deve repetir;
for i in range(10):
    print(i)

# Método 2: passando dois argumentos, um que representa o início das repetições e outro o limite superior (NÃO INCLUÍDO) do valor da variável de controle;
for i in range(0, 5):
    print(i)

# Método 3: Passando três argumentos, um que representa o início das repetições; outro, o limite superior (NÃO INCLUÍDO) do valor da variável de controle e um que representa o incremento.
for i in range(0, 20, 2):
    print(i)

# Exemplo de uso do break
disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)

# Exemplo de uso do continue
disciplina = "Linguagem de programação"
for c in disciplina:
    if c == 'a':
        continue
    else:
        print(c)