# Sistema de Controle de Estoque com Tratamento de Exceção
Este projeto implementa um sistema de controle de estoque simples utilizando conceitos de Orientação a Objetos e tratamento de exceções em Python.

# Classes:
        Produto:
            Atributos: nome (string), quantidade (inteiro), preco (float)
            Métodos:
                retirar_do_estoque(quantidade: int): Diminui a quantidade de produtos em estoque, lançando uma exceção customizada EstoqueInsuficiente caso a quantidade a ser retirada seja maior que a disponível.
                adicionar_ao_estoque(quantidade: int): Aumenta a quantidade de produtos em estoque, lançando uma exceção customizada QuantidadeInvalida caso a quantidade a ser adicionada seja negativa.
        Estoque:
            Atributos: produtos (lista de objetos Produto)
            Métodos:
                adicionar_produto(produto: Produto): Adiciona um novo produto ao estoque.
                remover_produto(nome_produto: string): Remove um produto do estoque pelo nome, lançando uma exceção customizada ProdutoNaoEncontrado caso o produto não seja encontrado.
                buscar_produto(nome_produto: string): Retorna o objeto Produto correspondente ao nome fornecido, lançando uma exceção customizada ProdutoNaoEncontrado caso o produto não seja encontrado.
        Exceções Customizadas:
            EstoqueInsuficiente: Lançada quando a quantidade a ser retirada do estoque é maior que a disponível.
            QuantidadeInvalida: Lançada quando a quantidade a ser adicionada ao estoque é negativa.
            ProdutoNaoEncontrado: Lançada quando um produto não é encontrado no estoque.
            
# Funcionamento:
        1. O sistema deve permitir ao usuário adicionar novos produtos ao estoque, informando o nome, a quantidade inicial e o preço.
        2. O usuário pode retirar produtos do estoque, informando o nome do produto e a quantidade desejada.
        3. O sistema deve tratar as seguintes exceções:
            EstoqueInsuficiente: Exibir uma mensagem informando que a quantidade solicitada não está disponível em estoque.
            QuantidadeInvalida: Exibir uma mensagem informando que a quantidade informada é inválida.
            ProdutoNaoEncontrado: Exibir uma mensagem informando que o produto não foi encontrado no estoque.
        4. O sistema deve exibir o estoque atualizado após cada operação.

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
