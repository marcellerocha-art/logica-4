def lista_tarefas():
    tarefas = []
    
    print("=" * 60)
    print("LISTA DE TAREFAS")
    print("=" * 60)
    print("Digite suas tarefas (ou 'fim' para encerrar):\n")
    
    while True:
        tarefa = input("Tarefa: ")
        
        if tarefa.lower() == 'fim':
            break
        
        tarefas.append(tarefa)
    
    print("\n" + "=" * 60)
    print("TAREFAS CADASTRADAS")
    print("=" * 60)
    
    if tarefas:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
        print(f"\nTotal de tarefas: {len(tarefas)}")
    else:
        print("Nenhuma tarefa cadastrada!")
    
    print("=" * 60)


if __name__ == "__main__":
    lista_tarefas()