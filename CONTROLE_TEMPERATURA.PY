def controle_temperaturas():
    celsius = []
    fahrenheit = []
    
    print("=" * 60)
    print("CONTROLE DE TEMPERATURAS")
    print("=" * 60)
    print("Digite temperaturas em Celsius (ou 'sair' para encerrar):\n")
    
    while True:
        try:
            entrada = input("Temperatura (°C): ")
            
            if entrada.lower() == 'sair':
                break
            
            temp_c = float(entrada)
            celsius.append(temp_c)
            
        except ValueError:
            print("❌ Erro! Digite um valor numérico válido\n")
    
    if not celsius:
        print("\nNenhuma temperatura cadastrada!")
        return
    
    for temp_c in celsius:
        temp_f = (temp_c * 9/5) + 32
        fahrenheit.append(temp_f)
    
    media_celsius = sum(celsius) / len(celsius)
    media_fahrenheit = sum(fahrenheit) / len(fahrenheit)
    
    print("\n" + "=" * 60)
    print("RESULTADO")
    print("=" * 60)
    
    print("\nTemperaturas em Celsius:")
    for i, temp in enumerate(celsius, 1):
        print(f"{i}. {temp}°C")
    
    print("\nTemperaturas em Fahrenheit:")
    for i, temp in enumerate(fahrenheit, 1):
        print(f"{i}. {temp:.2f}°F")
    
    print("\n" + "-" * 60)
    print(f"Média de Celsius: {media_celsius:.2f}°C")
    print(f"Média de Fahrenheit: {media_fahrenheit:.2f}°F")
    print("=" * 60)


if __name__ == "__main__":
    controle_temperaturas()