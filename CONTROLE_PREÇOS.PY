def controle_precos():
    precos = []
    
    print("=" * 60)
    print("CONTROLE DE PREÇOS")
    print("=" * 60)
    print("Digite 5 preços:\n")
    
    for i in range(1, 6):
        while True:
            try:
                preco = float(input(f"Preço {i}: R$ "))
                precos.append(preco)
                break
            except ValueError:
                print("❌ Erro! Digite um valor numérico válido")
    
    print("\n" + "=" * 60)
    print("RESULTADO")
    print("=" * 60)
    
    print(f"\nPreços cadastrados: {precos}")
    print(f"\nMaior preço: R$ {max(precos):.2f}")
    print(f"Menor preço: R$ {min(precos):.2f}")
    print("=" * 60)


if __name__ == "__main__":
    controle_precos()