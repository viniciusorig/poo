import datetime

class Cliente:
    def __init__(self, nome, cpf, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__repr__()
    def __repr__(self):
        print(f"Nome Titular: {self.__nome}\nCPF: {self.__cpf}\nNascimento: {self.__nascimento}")

class Banco:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.list = []

    def contasapp(self, conta):
        self.list.append(conta)

    def saque(self, cliente, valor)->bool:
        if(cliente.saldo == 0):
            print("Nao saldo eh zero nao eh possivel realizar o saque")
            cliente.operacao.append(f"Saque nao efetudo :: {date.today()}")
            return False
        if((cliente.saldo - valor) < 0):
            print("nao sera possivel realizar o saque pois seu saldo ficaria negativo")
            cliente.operacao.append(f"Saque nao efetudo :: {date.today()}")
            return False
        cliente.saldo -= valor
        cliente.operacao.append(f"Saque efetudo :: {date.today()}")
        return True
    
    def deposito(self, cliente, valor)->bool:
        cliente.saldo += valor
        cliente.operacao.append(f"deposito efetudo :: {date.today()}")
        return True
    
    def tranferencia(self, cliente_orig, cliente_dest, valor)->bool:
        if(self.saque(cliente_orig, valor) == False):
            print("naao foi possivel realizar a tranferencia pois a conta de origem nao tem saldo")
            return False
        self.deposito(cliente_dest, valor)
        cliente_orig.operacao.append(f"tranferencia efetuada para :: {cliente_dest} horario:: {date.today()}")
        return True

class Conta:
    def __init__(self, agencia, numero, saldo, cliente:'Cliente'):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        self.__repr__()
        self.operacaao = []

   def __repr__(self) -> str:
       print(f'''Agencia: {self.agencia}\nNumero: {self.numero}\nSaldo_atual: {self.saldo}''')

c1 = Cliente('vini','052', date(2002, 9, 12))
cc1 = Conta('3066', '29034', '0', c1)
