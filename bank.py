from datetime import date

class Cliente:
    def __init__(self, nome, cpf, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__repr__()
    def __repr__(self):
        print(f"Nome Titular: {self.__nome}\nCPF: {self.__cpf}\nNascimento: {self.__nascimento}")

class Banco:
    def saque(self, cliente, valor)->bool:
        if(cliente.saldo == 0):
            print("Nao saldo eh zero nao eh possivel realizar o saque")
            return False
        if((cliente.saldo - valor) < 0):
            print("nao sera possivel realizar o saque pois seu saldo ficaria negativo")
            return False
        
        cliente.saldo -= valor
        return True
    def deposito(self, cliente, valor)->bool:
        cliente.saldo += valor
        return True
    def tranferencia(self, cliente_orig, cliente_dest, valor)->True:
        if(self.saque(cliente_orig, valor) == False):
            print("naao foi possivel realizar a tranferencia pois a conta de origem nao tem saldo")
        self.deposito(cliente_dest, valor)

class Conta:
    def __init__(self, agencia, numero, saldo, cliente:'Cliente'):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        self.__repr__()
    def __repr__(self) -> str:
       print(f'''Agencia: {self.agencia}\nNumero: {self.numero}\nSaldo_atual: {self.saldo}''')

c1 = Cliente('vini','052', date(2002, 9, 12))
cc1 = Conta('3066', '29034', '0', c1)
