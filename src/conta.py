class Conta:
    def __init__(self, numero:int, saldo:float):
        self.numero = numero
        self.saldo = saldo + 100
        self.limite = 100
        self.lista_extrato = []
        
    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float): #Ao sacar um valor o limite da conta deve ser considerado
        if self.saldo - valor < 0 or valor < 0 or len(self.lista_extrato) >= 10:
          return False
        else:
            self.saldo -= valor
            self.lista_extrato.append(float(+valor))
            return True

    def depositar(self, valor: float):
        print(len(self.verExtrato()))
        if valor <= 0 or len(self.lista_extrato) >= 10:   #Depositar valores nao negativos deve ser permitido
            return False
        else:
            self.saldo += valor
            self.lista_extrato.append( float(+valor))
            return True

    def transferir(self, destino, valor:float):
        if self.saldo - valor < 0 or valor < 0 or len(self.lista_extrato ) >= 10:
            return False
        elif not isinstance(destino, Conta):
            return False
        else:
            if valor > self.saldo - self.limite:
                self.limite = self.limite - (valor - (self.saldo - self.limite))
            self.saldo -= valor
            self.lista_extrato.append(float(-valor))
            destino.depositar(valor)

        return True

    def verExtrato(self):
       return self.lista_extrato

