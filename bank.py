import datetime

class Cliente:
    def __init__(self, nome, cpf, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__repr__()
    def __repr__(self):
        f"Nome Titular: {self.__nome}\nCPF: {self.__cpf}\nNascimento: {self.__nascimento}"

class Operacao:
    def __init__(self, operacao) -> None:
        self.date = datetime.date.today()
        self.operacao = operacao
    def __repr__(self) -> str:
        return f"{self.operacao} // {self.date}"
    
class Banco:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
        self.list = []
        self.contas = []
    
    def __repr__(self) -> str:
        return f"Nome Banco {self.getname()}, Endereco {self.getedereco()}, Contas :\n{self.contas}, operacoes :\n{self.list}"

    def getname(self):
        return self.__nome
    
    def getedereco(self):
        return self.__endereco
    
    def setOperation(self, operacao:"Operacao"):
        self.list.append(operacao)

    def contasapp(self, conta:"Conta"):
        self.contas.append(conta)

class Conta:
    def __init__(self, agencia, numero, saldo, cliente:"Cliente", banco:"Banco"):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo
        self.__cliente = cliente
        self.__banco = banco
        self.getBank().contasapp(self)

    def __repr__(self) -> str:
       return f"Agencia: {self.getAgencia()}\nNumero: {self.getNumero()}\nSaldo_atual: {self.getSaldo()}"

    def getSaldo(self):
        return self.__saldo
    
    def getAgencia(self):
        return self.__agencia
    
    def getNumero(self):
        return self.__numero
    
    def getCliente(self):
        return self.__cliente
    
    def getBank(self):
        return self.__banco
    
    def setSaldo(self, valor):
        self.__saldo += valor
   
    def saque(self, valor)->bool:
        if(self.getSaldo() == 0 or (self.getSaldo() - valor) < 0):
            print("Nao eh possivel realizar o saque saldo 0")
            self.getBank().setOperation(Operacao("Sem saldo para saque"))
            
            return False
        
        self.setSaldoaldo = (valor * -1)
        self.getBank().setOperation(Operacao(f"Sem saldo para saque"))

        return True
    
    def deposito(self, valor)->bool:
        self.setSaldo = valor
        self.__banco.setOperation(Operacao("Deposito com exito"))

        return True
    
    def tranferencia(self, cliente_dest:"Conta", valor)->bool:
        if(self.saque(valor) == False):
            self.__banco.setOperation(Operacao("Erro de tranferencia :: Sem saldo"))
            return False
        
        cliente_dest.deposito(valor)
        
        self.__banco.setOperation(Operacao(f"tranferencia efetuada para :: {cliente_dest}"))
        cliente_dest.__banco.setOperation(Operacao(f"tranferencia recebida de :: {self}"))
        return True

b1 = Banco("penis", "rua do infeno 666")
cc1 = Conta('3066', '29034', 100, Cliente('vini','052', datetime.date(2002, 9, 12)), b1)

cc2 = Conta('3066', '29034', 0, Cliente('penis','052', datetime.date(2002, 9, 12)), b1)

cc1.saque(2)
cc2.deposito(2)
cc1.tranferencia(cc2, 50)

print(b1)