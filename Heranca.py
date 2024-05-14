class Pessoa:
    def __init__(self, nome="", endereco="", telefone=""):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getTelefone(self):
        return self.__telefone

    def setNome(self, nome):
        self.__nome = nome

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setTelefone(self, telefone):
        self.__telefone = telefone

class Fornecedor(Pessoa):
    def __init__(self, nome="", endereco="", telefone="", valorCredito=0, valorDivida=0):
        super().__init__(nome, endereco, telefone)
        self.__valorCredito = valorCredito
        self.__valorDivida = valorDivida

    def getValorCredito(self):
        return self.__valorCredito

    def getValorDivida(self):
        return self.__valorDivida

    def setValorCredito(self, valorCredito):
        self.__valorCredito = valorCredito

    def setvalorDivida(self, valorDivida):
        self.__valorDivida = valorDivida

    def obterSaldo(self):
        return self.__valorDivida - self.__valorDivida

class Empregado(Pessoa):
    def __init__(self, nome="", endereco="", telefone="", codigoSetor=0, salarioBase=0, imposto=0):
        super().__init__(nome, endereco, telefone)
        self.__codigoSetor = codigoSetor
        self.__salarioBase = salarioBase
        self.__imposto = imposto

    def getCodigoSetor(self):
        return self.__codigoSetor

    def getSalarioBase(self):
        return self.__salarioBase

    def getImposto(self):
        return self.__imposto

    def setCdogioSetor(self, codigoSetor):
        self.__codigoSetor = codigoSetor

    def setSalarioBase(self, salarioBase):
        self.__salarioBase = salarioBase

    def setImposto(self, imposto):
        self.__imposto = imposto

    def calcularSalario(self):
        salarioLiquido = self.__salarioBase - (self.__salarioBase*(self.__imposto/100))
        return salarioLiquido

class Administrador(Empregado):
    def __init__(self, nome="", endereco="", telefone="", codigoSetor=0, salarioBase=0, imposto=0, ajudaDeCusto=0):
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto)
        self.__ajudaDeCusto = ajudaDeCusto

    def getAjudaDeCusto(self):
        return self.__ajudaDeCusto

    def setAjudaDeCusto(self, ajudaDeCusto):
        self.__ajudaDeCusto = ajudaDeCusto

    def calcularSalario(self):
        salarioLiquido = super().calcularSalario() + self.__ajudaDeCusto
        return salarioLiquido

class Operario(Empregado):
    def __init__(self, nome="", endereco="", telefone="", codigoSetor=0, salarioBase=0, imposto=0, valorProducao=0, comissao=0):
        super().__init__(nome, endereco, telefone, imposto, codigoSetor, salarioBase)
        self.__valorProducao = valorProducao
        self.__comissao = comissao

    def getValorProducao(self):
        return self.__valorProducao

    def getComissao(self):
        return self.__comissao

    def setValorProducao(self, valorProducao):
        self.__valorProducao = valorProducao

    def setComissao(self, comissao):
        self.__comissao = comissao

    def calcularSalario(self):
        salarioLiquido = super().calcularSalario() + (self.__valorProducao * (self.__comissao / 100))
        return salarioLiquido

class Vendedor(Empregado):
    def __init__(self, nome="", endereco="", telefone="", codigoSetor=0, salarioBase=0, imposto=0, valorVendas=0, comissao=0):
        super().__init__(nome, endereco, telefone, codigoSetor, salarioBase, imposto)
        self.__valorVendas = valorVendas
        self.__comissao = comissao
        
    def getValorVendas(self):
        return self.__valorVendas
    
    def getComissao(self):
        return self.__comissao
    
    def setValorVendas(self, valorVendas):
        self.__valorVendas = valorVendas
    
    def setComissao(self, comissao):
        self.__comissao = comissao
        
    def calcularSalario(self):
        salarioLiquido = super().calcularSalario() + (self.__valorVendas * (self.__comissao / 100))
        return salarioLiquido

# Testando as classes

# Fornecedor
fornecedor = Fornecedor("Fornecedor 1", "Rua A", "123456789", 5000, 2000)
print("Nome:", fornecedor.getNome())
print("Endereço:", fornecedor.getEndereco())
print("Telefone:", fornecedor.getTelefone())
print("Valor de Crédito:", fornecedor.getValorCredito())
print("Valor da Dívida:", fornecedor.getValorDivida())
print("Saldo:", fornecedor.obterSaldo())

# Empregado
empregado = Empregado("Funcionário 1", "Rua B", "987654321", 1001, 3000, 10)
print("\nNome:", empregado.getNome())
print("Endereço:", empregado.getEndereco())
print("Telefone:", empregado.getTelefone())
print("Código do Setor:", empregado.getCodigoSetor())
print("Salário Base:", empregado.getSalarioBase())
print("Imposto (%):", empregado.getImposto())
print("Salário Líquido:", empregado.calcularSalario())
print()

# Administrador
admin = Administrador("Admin 1", "Rua C", "456789123", 456, 3000, 15, 500)
print("Administrador:")
print("Nome:", admin.getNome())
print("Endereço:", admin.getEndereco())
print("Telefone:", admin.getTelefone())
print("Código do Setor:", admin.getCodigoSetor())
print("Salário Base:", admin.getSalarioBase())
print("Imposto (%):", admin.getImposto())
print("Ajuda de Custo:", admin.getAjudaDeCusto())
print("Salário Líquido:", admin.calcularSalario())
print()

# Operario
operario = Operario("Operário 1", "Rua D", "987123456", 789, 1500, 5, 1000, 10)
print("Operário:")
print("Nome:", operario.getNome())
print("Endereço:", operario.getEndereco())
print("Telefone:", operario.getTelefone())
print("Código do Setor:", operario.getCodigoSetor())
print("Salário Base:", operario.getSalarioBase())
print("Imposto (%):", operario.getImposto())
print("Valor da Produção:", operario.getValorProducao())
print("Comissão (%):", operario.getComissao())
print("Salário Líquido:", operario.calcularSalario())
print()

# Vendedor
vendedor = Vendedor("Vendedor 1", "Rua E", "987654321", 987, 2500, 12, 5000, 8)
print("Vendedor:")
print("Nome:", vendedor.getNome())
print("Endereço:", vendedor.getEndereco())
print("Telefone:", vendedor.getTelefone())
print("Código do Setor:", vendedor.getCodigoSetor())
print("Salário Base:", vendedor.getSalarioBase())
print("Imposto (%):", vendedor.getImposto())
print("Valor das Vendas:", vendedor.getValorVendas())
print("Comissão (%):", vendedor.getComissao())
print("Salário Líquido:", vendedor.calcularSalario())
