# Importa todas as classes e métodos necessários da bookbase
from bookbase import *

# Função para facilitar a entrada de dados do usuário
def input_dados() -> List[any]:
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    editora = input("Editora: ")
    idioma = input("Idioma: ")
    isbn = input("ISBN: ")
    data_pub = input("Ano de publicação: ")
    num_pag = int(input("Número de páginas: "))

    dados = [titulo, autor, genero, editora, idioma, isbn, data_pub, num_pag]
    return dados

# Menu principal da interface 
def menu() -> None:
    # Lê/cria o arquivo da base e o guarda numa variável 
    base = BookBase("arquivo_base")
    print()
    print("BEM VINDO AO BOOKBASE!")
    print("Uma pequena base de dados para seus livros")
    print()
    while True:
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Substituir item")
        print("4. Apagar base")
        print("5. Consultar base")
        print("6. Sair")
        print()
    
        escolha = int(input("> "))
        print()

        if escolha == 1:
            # Lê os dados do usuário e adiciona uma nova entrada
            base.add_linha(input_dados())

        if escolha == 2:
            # Seleciona o ID da linha desejada e a remove
            id_linha = int(input("ID da linha que será removida: "))
            print()
            base.rm_linha(id_linha)
            print("Linha removida com sucesso!")

        if escolha == 3: 
            # Seleciona o ID da linha que será sobrescrita e a sobrescreve
            id_linha = int(input("ID da linha que será sobrescrita: "))
            print()
            base.ow_linha(id_linha, input_dados())
            print("Linha sobrescrita com sucesso!")

        if escolha == 4: 
            # Confirmação para evitar tristezas 
            print("Você tem certeza que quer fazer isso? (y/n)")
            certeza = input("> ").lower() 
            if certeza == "y": 
                # Deleta toda a base de dados 
                base.del_db()
        
        if escolha == 5: 
            # Caso o usuário queira, a base será mostrada em ordem alfabética 
            print("Deseja ver a base ordenada em ordem alfabética? (y/n)")
            ordenada = input("> ")
            print()
            base.ver(ordenada)
            input("")

        if escolha == 6: 
            break

        print()

menu()
print()
input("Aperte qualquer tecla para sair...")