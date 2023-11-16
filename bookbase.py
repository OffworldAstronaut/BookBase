# Manipulação da base 
import pandas as pd 
# Tipagem especial 
from typing import List 
# Escrever no terminal de maneira organizada
from tabulate import tabulate 
# Copiar arquivos 
from shutil import copy
# Utilidades do sistema operacional 
import os

class BookBase:
    def __init__(self, arquivo : str) -> None: 
        """Inicializa uma instância da classe BookBase

        Args:
            arquivo (str): Nome do arquivo que servirá como base de dados
        """
        # O nome da base propriamente dito é a str 'arquivo' recebida 
        self.nome_base = arquivo
        # O nome do arquivo realmente tem a extensão .xlsx no final 
        self.nome_arquivo = arquivo + '.xlsx'
        # Se o arquivo já existe, não faça nada
        if os.path.exists(self.nome_arquivo):
            pass
        # Se o arquivo não existe, crie ele com base no arquivo padrão
        else:
            copy("default.xlsx", self.nome_arquivo)
        # Leia o arquivo criado/previamente existente como dataframe
        self.tabela = pd.DataFrame(pd.read_excel(self.nome_arquivo))
        # Classifique o índice de cada linha como a coluna "ID"
        self.tabela.set_index("ID")
        

    def add_linha(self, dados : List[any]) -> None:
        """Adiciona uma linha no final da base de dados 

        Args:
            dados (List[any]): Lista contendo os dados a serem adicionados de forma ordenada
        """
        # Insere nos dados do livro a ser criado um ID único com base na sua posição da tabela 
        dados.insert(0, len(self.tabela.index))
        # Adiciona esse livro na tabela 
        self.tabela.loc[len(self.tabela.index)] = dados
        # Escreve para o arquivo .xlsx
        self.salvar()


    def rm_linha(self, id_linha : int) -> pd.DataFrame: 
        """Remove uma linha qualquer da base de dados

        Args:
            tabela (pd.DataFrame): tabela da qual a linha será removida
            id_linha (int): ID da linha que será removida 

        Returns:
            pd.DataFrame: Tabela sem a linha que foi removida
        """
        # Sobrescreve a tabela com uma cópia dela que possui todos os IDs diferentes do ID que será removido 
        self.tabela = self.tabela[self.tabela["ID"] != id_linha]
        # Escreve para o arquivo .xlsx
        self.salvar()

    def ow_linha(self, id_linha : int, novos_dados : List[any]) -> None: 
        """Sobreescreve uma linha qualquer da base de dados

        Args:
            id_linha (int): ID da linha que será reescrita 
            novos_dados (List[any]): Dados que irão sobreescrever os antigos
        """
        # Localiza a linha que será sobrescrita e salva seu ID
        id_item = self.tabela.at[id_linha, "ID"]
        # Insere esse ID nos novos dados que serão escritos 
        novos_dados.insert(0, id_item)
        # Localiza a linha que será sobrescrita e insere os novos dados
        self.tabela.loc[id_linha] = novos_dados
        # Escreve para o arquivo .xlsx
        self.salvar()

    def salvar(self) -> None: 
        """Escreve as alterações feitas no DataFrame carregado para o arquivo .xlsx da base"""
        self.tabela.to_excel(self.nome_arquivo, index=False)

    def ver(self, ordenada : str) -> None:
        """Imprime de forma organizada na tela a base de dados para o usuário

        Args:
            ordenada (str): variável para indicar se a lista será ordenada em ordem alfabética ou não
        """
        # Facilitador de escrita 
        tabela = self.tabela
        if ordenada == 'y': 
            # Caso o usuário tenha desejado, organize a tabela em ordem alfabética
            tabela = tabela.sort_values("TITULO")
        print(tabulate(tabela, headers=tabela.head(), tablefmt='simple_grid', showindex=False))


    def del_db(self) -> None: 
        """Apaga todas as entradas da base por meio de aplicações sucessivas do método rm_linha()"""
        for i in range(0, len(self.tabela)): 
            self.rm_linha(i)