class Conta:
    def __init__(self, numero:int, saldo = 0, limite = 100):
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo + self.limite

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float):
        if valor > 0:
            if valor > self.saldo:
                self.saldo -= valor - self.limite
            else:
                self.saldo -= valor
            return True
        return  False

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def transferir(self, destino, valor:float):
        if valor > self.saldo:
            return False
        else:
            if valor > 0:
                retirou = self.sacar(valor)
                if retirou:
                    self.saldo -= valor
                    destino.depositar(valor)
                    return True
                else:
                    return False
            else:
                return False

    def verExtrato(self):
        print("numero:{}\nsaldo:{}".format(self.numero, self.getSaldo()))
