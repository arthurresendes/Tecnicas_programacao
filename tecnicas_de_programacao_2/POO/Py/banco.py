from abc import abstractmethod, ABC

class Conta(ABC):
    def __init__(self,nome:str,saldo: float,limite:float):
        self._nome = nome
        self._saldo = saldo
        self._limite = limite
        
    @abstractmethod
    def tipo_conta(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, nome, saldo, limite):
        super().__init__(nome, saldo, limite)
    
    
    def tipo_conta(self):
        return "Essa é uma conta corrente"
    def get_limite(self):
        return f"Seu limite por deposito é de {self._limite}"
    def get_saldo(self):
        return self._saldo
    def set_saldo(self,valor: int):
        if valor <= self._limite:
            self._saldo += valor
        
class ContaDigital(Conta):
    def __init__(self, nome, saldo, limite):
        super().__init__(nome, saldo, limite)
    
    
    def tipo_conta(self):
        return "Essa é uma conta digital"
    def get_limite(self):
        return f"Seu limite por deposito é de {self._limite}"
    def get_saldo(self):
        return self._saldo
    def set_saldo(self,valor: float):
        if valor <= self._limite:
            self._saldo += valor
        else:
            pass


contaC = ContaCorrente('Arthur', 1000.99, 2000.00)
print(contaC.tipo_conta())
print(contaC.get_limite())
print(contaC.get_saldo())
contaC.set_saldo(1000)
print(contaC.get_saldo())
contaD = ContaDigital('Arthur', 1000.99, 2000.00)
print(contaD.tipo_conta())
print(contaD.get_limite())
print(contaD.get_saldo())
contaD.set_saldo(1000)
print(contaD.get_saldo())