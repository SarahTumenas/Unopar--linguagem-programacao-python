class PrimeiraClasse:  # Declaração da Classe

    @staticmethod
    def imprimir_mensagem(nome):  ##Criando um método
        print(f"Olá {nome}, seja bem vindo!")


objeto1 = PrimeiraClasse()  # Instanciandoum objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('Aluno')  # ivocando o método

print("\t------------\t")


class Televisao:
    def __init__(self):
        self.volume = 10

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1


tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)

tv.aumentar_volume()
print("Volume atual = ", tv.volume)

print("\t------------\t")


class ContaCorrente:

    def __init__(self):
        self._saldo = None

    def depositar(self, valor):
        self._saldo += valor

    def consultar_saldo(self):
        return self._saldo


print("\t------------\t")
