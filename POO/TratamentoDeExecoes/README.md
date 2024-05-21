# Sistema de Controle de Estoque com Tratamento de Exceção
Este projeto implementa um sistema de controle de estoque simples utilizando conceitos de Orientação a Objetos e tratamento de exceções em Python.

# Descrição
O sistema permite:

    Cadastrar produtos com nome, quantidade e preço.
    Adicionar e remover produtos do estoque.
    Consultar produtos por nome.
    Controlar o estoque, lançando exceções em casos de:
            Tentativa de retirar quantidade maior que a disponível.
            Tentativa de adicionar quantidade negativa.
            Busca por produto não cadastrado.
            
# Exceções Customizadas
    EstoqueInsuficiente: Lançada ao tentar retirar quantidade maior que a disponível.
    QuantidadeInvalida: Lançada ao tentar adicionar quantidade negativa ao estoque.
    ProdutoNaoEncontrado: Lançada ao buscar um produto não cadastrado.
    
# Exemplo de Uso
      # Criando um produto
      produto1 = Produto("Camiseta", 10, 20.00)

      # Criando o estoque
      estoque = Estoque()

      # Adicionando o produto ao estoque
      estoque.adicionar_produto(produto1)

      # Tentando retirar uma quantidade maior do que a disponível
      try:
          produto1.retirar_do_estoque(15)
      except EstoqueInsuficiente:
          print("Erro: Quantidade insuficiente em estoque.")

      # Exibindo o estoque atualizado
          print(estoque.produtos)
