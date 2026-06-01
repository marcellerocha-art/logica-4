# 📋 Logica-4: Lista de Compras

Exercícios de lógica com Python - Sistema de Gerenciamento de Lista de Compras

## 📝 Descrição

Este projeto implementa um **sistema de lista de compras interativo** desenvolvido em Python. O programa permite que o usuário adicione, pesquise, remova, altere e visualize produtos em uma lista de compras através de um menu intuitivo.

## 🎯 Funcionalidades

- ✅ **Adicionar produtos** - Insira novos itens à sua lista de compras
- 🔍 **Pesquisar produto** - Verifique se um produto está na lista
- ❌ **Remover produto** - Delete itens da lista
- ✏️ **Alterar produto** - Modifique o nome de um produto existente
- 📊 **Listar produtos** - Visualize todos os itens da lista
- 🚪 **Sair** - Encerre o programa

## 🚀 Como Usar

### Pré-requisitos
- Python 3.x instalado no seu sistema

### Executando o programa

```bash
python LISTA_COMPRAS.py
```

### Instruções de Uso

1. Ao iniciar, você verá o menu principal com 6 opções
2. Digite o número da opção desejada (1-6)
3. Siga as instruções na tela
4. Para sair do programa, escolha a opção 6

#### Exemplo de uso:

```
======================================
LISTA DE COMPRAS - MENU
======================================
1 - Adicionar à lista
2 - Pesquisar item
3 - Remover item
4 - Alterar item
5 - Listar produtos
6 - Sair
======================================

Escolha uma opção (1-6): 1

Digite produtos para compra (ou 'sair' para encerrar):

Produto: maçã
✓ 'maçã' adicionado à lista

Produto: leite
✓ 'leite' adicionado à lista

Produto: sair
```

## 📁 Estrutura do Código

### Funções Principais

| Função | Descrição |
|--------|-----------|
| `adicionar_produtos(lista)` | Adiciona novos produtos à lista |
| `pesquisar_produto(lista)` | Busca um produto específico |
| `remover_produto(lista)` | Remove um produto da lista |
| `alterar_produto(lista)` | Modifica o nome de um produto |
| `listar_produtos(lista)` | Exibe todos os produtos |
| `menu()` | Gerencia o loop principal e opções |

## 💡 Conceitos de Lógica Abordados

- Estruturas de controle (loops e condicionais)
- Manipulação de listas em Python
- Funções e parâmetros
- Entrada e saída de dados
- Busca e modificação de elementos em listas

## 🔧 Melhorias Futuras

- [ ] Persistência de dados em arquivo
- [ ] Sistema de categorias para produtos
- [ ] Quantidade e preço de itens
- [ ] Interface gráfica (tkinter)
- [ ] Exportar lista em PDF

## 📝 Autor

**marcellerocha-art**

## 📄 Licença

Este projeto é um exercício educacional de lógica com Python.

---

**Desenvolvido para fins de aprendizado de Python e lógica de programação** 🐍
