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