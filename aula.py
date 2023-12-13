class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo  = saldo

    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor;
        else:
            print("saldo insuficiente");

class contaCC(Conta):
    def __init__(self, numero, saldo=0):
        Conta.__init__(numero, saldo)

class contaPP(Conta):
    def __init__(self, numero, saldo=0):
        Conta.__init__(numero, saldo)

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade  = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        Pessoa.__init__(self, nome, idade)
        self.salario = salario
    
    def __str__(self):
        return f"{self.nome}, {self.idade}, Salario {self.salario:.2f}"
       
class FuncCC(Pessoa, Conta):
    def __init__(self, nome, idade, salario, numero, saldo = 0):
        Funcionario.__init__(nome, idade, salario)
        Conta.__init__(numero, saldo)

# fazer a implementação da classe autentica herança multipla do diretetror e gerente com classe entregar ate amanha, quinta feira as 23h59  (usar o minimo possivel) no email
class Diretor(FuncCC):
    def __init__(self, nome, idade, salario, numero, bonifica, nivel,saldo=0):
        Funcionario.__init__(self, nome, idade, salario)
        Conta.__init__(self, numero, saldo)
        self.bonifica = bonifica 
        self.nivel = nivel
    def login (self):
        pass

class Gerente(FuncCC):
    def __init__(self, nome, idade, salario, numero, bonifica, nivel, saldo=0):
        Funcionario.__init__(self, nome, idade, salario)
        Conta.__init__(self, numero, saldo)
        self.bonifica = self.salario * 1.15
        self.nivel = nivel
    def login (self):
        pass

class Cliente(Pessoa, Conta):
    def __init__(self,nome, idade, numero, saldo = 0):
        Pessoa.__init__(self,nome,idade)
        Conta.__init__(self,numero, saldo)

    def __str__(self):
        return f"{self.nome}, {self.idade}, CC {self.numero}, Saldo {self.saldo:.2f}"

class Autentica(Diretor):
    def __init__(self, funcionario):
        self.x = Diretor(None, None, None, None, None, None, None)
        self.acesso = []
        if type(funcionario) == type(self.x):
            self.acesso = ["root", 10]
        else:
            self.acesso = ["root", 5]

    def __str__(self):
        return f"o usuario permitido {self.acesso[0]}, nivel de acesso ao website eh {self.acesso[1]}"
      
cliente_beto = Cliente("beto",20,1234,400)
g = Gerente("meme", 40, 130000, 123, 20, 2, 15.00)

a = Autentica(g)

print(f"a autencidade do usuario {g.nome} :: {a}")
h = Diretor("hehe", 60, 33333, 2524, 45, 2, 300.00)

b = Autentica(h)

print(f"a autencidade do usuario {h.nome} :: {b}")
