def adicionar_produtos(lista):
    print("\nDigite produtos para compra (ou 'sair' para encerrar):\n")
    
    while True:
        produto = input("Produto: ").lower()
        
        if produto == 'sair':
            break
        
        if produto:
            lista.append(produto)
            print(f"✓ '{produto}' adicionado à lista\n")


def pesquisar_produto(lista):
    produto = input("\nDigite o produto a pesquisar: ").lower()
    
    if produto in lista:
        print(f"✓ Produto encontrado: '{produto}'")
    else:
        print(f"❌ Produto não encontrado: '{produto}'")


def remover_produto(lista):
    produto = input("\nDigite o produto a remover: ").lower()
    
    if produto in lista:
        lista.remove(produto)
        print(f"✓ Produto encontrado")
        print(f"✓ '{produto}' removido da lista")
    else:
        print(f"❌ Produto não encontrado: '{produto}'")


def alterar_produto(lista):
    produto_antigo = input("\nDigite o produto a alterar: ").lower()
    
    if produto_antigo in lista:
        indice = lista.index(produto_antigo)
        produto_novo = input("Digite o novo nome do produto: ").lower()
        lista[indice] = produto_novo
        print(f"✓ Produto alterado com sucesso")
        print(f"  '{produto_antigo}' → '{produto_novo}'")
    else:
        print(f"❌ Produto não encontrado: '{produto_antigo}'")


def listar_produtos(lista):
    print("\n" + "=" * 60)
    print("LISTA DE COMPRAS")
    print("=" * 60)
    
    if not lista:
        print("Lista vazia")
    else:
        for i, produto in enumerate(lista, 1):
            print(f"{i}. {produto}")
    
    print("=" * 60)


def menu():
    lista = []
    
    while True:
        print("\n" + "=" * 60)
        print("LISTA DE COMPRAS - MENU")
        print("=" * 60)
        print("1 - Adicionar à lista")
        print("2 - Pesquisar item")
        print("3 - Remover item")
        print("4 - Alterar item")
        print("5 - Listar produtos")
        print("6 - Sair")
        print("=" * 60)
        
        opcao = input("\nEscolha uma opção (1-6): ")
        
        if opcao == '1':
            adicionar_produtos(lista)
        
        elif opcao == '2':
            pesquisar_produto(lista)
        
        elif opcao == '3':
            remover_produto(lista)
        
        elif opcao == '4':
            alterar_produto(lista)
        
        elif opcao == '5':
            listar_produtos(lista)
        
        elif opcao == '6':
            print("\nPrograma encerrado com sucesso!")
            break
        
        else:
            print("\n❌ Opção inválida! Digite uma opção entre 1 e 6")


if __name__ == "__main__":
    menu()