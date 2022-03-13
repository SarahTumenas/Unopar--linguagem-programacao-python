# A função eval() usada no código recebe # como entrada uma string digitada pelo # usuário, que nesse caso é uma equação  linear.
# Essa entrada é analisada e avaliada como uma expressão Python pela função eval().
# Veja que, para cada valor de x, a fórmula é executada como uma expressão matemática (linha 8) e retorna um valor diferente.
# Prudência para o uso, pois é fácil alguém externo à aplicação fazer uma "injection" de código intruso.

a = 2
b = 1

equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\nA entrada do usuário{equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")

# A função recebe dois parâmetros. Esses parâmetros são variáveis locais, ou seja, são variáveis que existem somente dentro da função.
# Na linha 2, imprimimos uma mensagem usando as variáveis passadas como parâmetro e na linha 5, invocamos a função,
# passando como parâmetros dois valores do tipo string.
# O valor "Python" vai para o primeiro parâmetro da função e o valor "Engenharia de Software" vai para o segundo parâmetro.

def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")
imprimir_mensagem("Python", "Engenharia de Software")

# Funções com parâmetros definidos e indefinidos
# Sobre os argumentos que uma função pode receber, para nosso estudo, vamos classificar em seis grupos:
# 01. Parâmetro posicional, obrigatório, sem valor default (padrão), tentar um invocar a função, sem passar os parâmetros, acarreta um erro.

def somar(a, b):
    return a + b
r = somar(2, 3)
print(r)

# 02. Parâmetro posicional, obrigatório, com valor default (padrão), quando a função for invocada, caso nenhum valor seja passado, o valor default é utilizado.

def calcular_desconto(valor, desconto=0): # O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25) # Aplicar desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")

# 03. Parâmetro nominal, obrigatório, sem valor default (padrão).
# Não mais importa a posição dos parâmetros, pois eles serão identificados pelo nome, a chamada da função é obrigatório passar todos os valores e sem valor default
def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()
texto = converter_maiuscula(flag_maiuscula=True, texto="João") # Passagem nominal de parâmetros
print(texto)

# 04.Parâmetro nominal, obrigatório, com valor default (padrão), nesse grupo os parâmetros podem possuir valor default.
def converter_minuscula(texto, flag_minuscula=True): # O parâmetro flag_minuscula possui True como valor default
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()
texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")
print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")

# 05. Parâmetro posicional e não obrigatório (args), a passagem de valores é feita de modo posicial,porém a quantidade não é conhecida.

def imprimir_parametros(*args):
    qtde_parametros = len(args)

    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros("São Paulo", 10, 23.78, "João")
print("\nChamada 2")
imprimir_parametros(10, "São Paulo")

# 06. Parâmetro nominal e não obrigatório (kwargs), agora a passagem é feita de modo nominal e não posicional, o que nos permite acessar tanto o valor do parâmetro
# quanto o nome da variável que o armazena.

def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")
print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)

# Funções anônimas em Python
# Uma função anônima é uma função que não é construída com o "def" e, por isso, não possui nome.
# Esse tipo de construção é útil, quando a função faz somente uma ação e é usada uma única vez.
# Poderoso recurso da linguagem Python: a expressão "lambda".

somar = lambda x, y: x + y
somar(x=5, y=3)