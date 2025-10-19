from biblioteca import biblioteca

def menu():
    print("\n--- Menu Biblioteca ---")
    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Usuário")
    print("3 - Listar Livros")
    print("4 - Emprestar Livro")
    print("5 - Devolver Livro")
    print("0 - Sair")

biblioteca = biblioteca()

while True:
    menu()
    opcao = input('Escolha uma opçao: ')
    if opcao == "1":
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        biblioteca.adicionar_livro(titulo, autor)
    elif opcao == "2":
        nome = input("Nome do usuário: ")
        biblioteca.adicionar_usuario(nome)
    elif opcao == "3":
        biblioteca.listar_livros()
    elif opcao == "4":
        try:
            id_livro = int(input("ID do livro para emprestar: "))
            biblioteca.emprestar_livro(id_livro)
        except ValueError:
            print("ID inválido.")
    elif opcao == "5":
        try:
            id_livro = int(input("ID do livro para devolver: "))
            biblioteca.devolver_livro(id_livro)
        except ValueError:
            print("ID inválido.")
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")
