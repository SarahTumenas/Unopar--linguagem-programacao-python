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