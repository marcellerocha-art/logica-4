def cadastrar_convidados():
    convidados = []
    
    print("=" * 60)
    print("CADASTRO DE CONVIDADOS")
    print("=" * 60)
    print("Cadastre 5 convidados:\n")
    
    for i in range(1, 6):
        nome = input(f"Convidado {i}: ")
        convidados.append(nome)
    
    print("\n" + "=" * 60)
    print("LISTA DE CONVIDADOS")
    print("=" * 60)
    
    for i, nome in enumerate(convidados, 1):
        print(f"{i}. {nome}")
    
    print("\n" + "=" * 60)
    print(f"Total de convidados: {len(convidados)}")
    print("=" * 60)


if __name__ == "__main__":
    cadastrar_convidados()