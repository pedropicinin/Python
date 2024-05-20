class EstoqueInsuficiente(Exception):
    pass

class QuantidadeInvalida(Exception):
    pass

class ProdutoNaoEncontrado(Exception):
    pass

class Produto:
    def __init__(self, nome="", quantidade=0, preco=0.0):
        self.nome = nome
        self.quantidade = int(quantidade)
        self.preco = float(preco)
    
    def retirar_do_estoque(self, quantidade):
        if quantidade > self.quantidade:
            raise EstoqueInsuficiente("Quantidade insuficiente em estoque.")
        self.quantidade -= quantidade
        
    def adicionar_ao_estoque(self, quantidade):
        if quantidade < 0:
            raise QuantidadeInvalida("Quantidade inválida para adicionar ao estoque.")
        self.quantidade += quantidade
        
    def __str__(self):
        return (f"Produto: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}")

class Estoque:
    def __init__(self):
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def remover_produto(self, nome_produto):
        produto = self.buscar_produto(nome_produto)
        self.produtos.remove(produto)
    
    def buscar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                return produto
        raise ProdutoNaoEncontrado("Produto não encontrado no estoque.")
    
    def __str__(self):
        if not self.produtos:
            return "Estoque vazio."
        return "\n".join(str(produto) for produto in self.produtos)
    
def main():
    estoque = Estoque()
    
    while True:
        print("1 - Adicionar Produto")
        print("2 - Retirar Produto")
        print("3 - Exibir estoque atualizado")
        print("4 - Sair")
        opcao = input("Opção: ")
        
        if opcao == "1":
            nome = input("Nome do Produto: ")
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço: "))
            try:
                produto = Produto(nome, quantidade, preco)
                estoque.adicionar_produto(produto) 
            except QuantidadeInvalida as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            nome = input("Nome do Produto: ")
            quantidade = int(input("Quantidade para retirar: "))
            try:
                produto = estoque.buscar_produto(nome)
                produto.retirar_do_estoque(quantidade)
            except EstoqueInsuficiente as e:
                print(f"Erro: {e}")
            except ProdutoNaoEncontrado as e:
                print(f"Erro: {e}")
        elif opcao == "3":
            print("Estoque atualizado: ")
            print(estoque)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
