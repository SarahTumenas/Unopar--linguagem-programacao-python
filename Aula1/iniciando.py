nome = input("Digite um nome: ")
print("Olá %s, bem vindo a disciplina de programação. parabéns pelo seu primeiro hello world!" % (nome))

# função format

print("Olá {}, bem vindo a disciplina de Programação. Parabéns pelo seu Hello world!".format(nome))

# strings formatadas

print(f"Olá {nome},  bem vindo a disciplina de Programação. Parabéns pelo seu Hello world!")

# Qual o resultado armazenado na variável operacao_1 : 25 ou 17?
operacao_1 = 2 + 3 * 5

# Qual o resultado armazenado na variável operacao_2 : 25 ou 17?
operacao_2 = (2+3) * 5

# Qual o resultado armazenado na variável operacao_3 : 4 ou 1?
operacao_3 = 4 / 2 ** 2

# Qual o resultado armazenado na variável operacao_4 : 1 ou 5?
operacao_4 = 13 % 3 + 4

print(f"Resultado da operacao_1 = {operacao_1}")
print(f"Resultado da operacao_2 = {operacao_2}")
print(f"Resultado da operacao_3 = {operacao_3}")
print(f"Resultado da operacao_4 = {operacao_4}")

a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

print(type(a))
print(type(b))
print(type(c))
print(type(x))

 # aqui fazemos a conversão da string para o tipo numérico
x = float(x)

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")
print(type(a))
print(type(b))
print(type(c))
print(type(x))