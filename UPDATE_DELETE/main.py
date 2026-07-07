import sqlite3
from pathlib import Path


# Caminho do banco de dados.
# Assim o Python sempre usa o escola.db que esta na mesma pasta deste arquivo.
CAMINHO_BANCO = Path(__file__).with_name('escola.db')


def conectar():
    """Cria a conexao com o banco escola.db."""
    return sqlite3.connect(CAMINHO_BANCO)


def mostrar_alunos(mensagem):
    # Funcao para visualizar os dados depois de cada comando.
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT ID, Nome, Email, Cidade FROM Alunos ORDER BY ID')
    alunos = cursor.fetchall()

    print('=' * 90)
    print(mensagem)
    print(alunos)

    conexao.close()


def criar_tabela():
    # Criando a tabela Alunos, caso ela ainda nao exista.
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Alunos(
            ID INTEGER PRIMARY KEY,
            Nome TEXT,
            Email TEXT,
            Cidade TEXT
        )
    ''')

    conexao.commit()
    conexao.close()


def inserir_alunos():
    # Inserindo alunos para testar UPDATE e DELETE.
    # INSERT OR REPLACE evita erro caso o ID ja exista no banco.
    conexao = conectar()
    cursor = conexao.cursor()

    alunos = [
        (10, 'Joao Silva', 'joao@email.com', 'Salvador'),
        (20, 'Maria Oliveira', 'maria@email.com', 'Recife'),
        (30, 'Pedro Santos', 'pedro@email.com', 'Fortaleza'),
        (40, 'Ana Costa', 'ana@email.com', 'Curitiba'),
    ]

    cursor.executemany('''
        INSERT OR REPLACE INTO Alunos(ID, Nome, Email, Cidade)
        VALUES (?, ?, ?, ?)
    ''', alunos)

    conexao.commit()
    conexao.close()


def atualizar_perfil(aluno_id, novo_nome, novo_email, nova_cidade):
    # UPDATE altera dados que ja existem na tabela.
    # O WHERE e muito importante para atualizar apenas o aluno correto.
    conexao = conectar()
    cursor = conexao.cursor()

    sql_update = '''
        UPDATE Alunos
        SET Nome = ?, Email = ?, Cidade = ?
        WHERE ID = ?
    '''

    cursor.execute(sql_update, (novo_nome, novo_email, nova_cidade, aluno_id))
    conexao.commit()

    print(f'Perfil do aluno {aluno_id} atualizado.')
    conexao.close()


def atualizar_cidade_por_nome(nome, nova_cidade):
    # Tambem podemos atualizar usando outro campo no WHERE.
    # Neste exemplo, alteramos a cidade do aluno pelo nome.
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE Alunos
        SET Cidade = ?
        WHERE Nome = ?
    ''', (nova_cidade, nome))

    conexao.commit()
    print(f'Cidade atualizada para o aluno {nome}.')
    conexao.close()


def deletar_aluno(aluno_id):
    # DELETE remove registros da tabela.
    # Com WHERE, removemos somente o aluno escolhido.
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM Alunos WHERE ID = ?', (aluno_id,))

    conexao.commit()
    print(f'Aluno {aluno_id} deletado.')
    conexao.close()


def deletar_por_cidade(cidade):
    # Podemos deletar usando uma condicao de texto.
    # Aqui removemos todos os alunos de uma cidade especifica.
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM Alunos WHERE Cidade = ?', (cidade,))

    conexao.commit()
    print(f'Alunos da cidade {cidade} deletados.')
    conexao.close()


# =============================== CUIDADO ===============================

# UPDATE sem WHERE atualiza TODOS os registros da tabela.
# Exemplo perigoso:
# cursor.execute('UPDATE Alunos SET Cidade = "Sao Paulo"')

# DELETE sem WHERE apaga TODOS os registros da tabela.
# Exemplo perigoso:
# cursor.execute('DELETE FROM Alunos')


# =============================== EXECUCAO ===============================

criar_tabela()
inserir_alunos()
mostrar_alunos('Alunos inseridos no banco:')

atualizar_perfil(10, 'Carlos Eduardo', 'carlos.eduardo@email.com', 'Sao Paulo')
mostrar_alunos('Depois do UPDATE por ID:')

atualizar_cidade_por_nome('Maria Oliveira', 'Maceio')
mostrar_alunos('Depois do UPDATE por Nome:')

deletar_aluno(30)
mostrar_alunos('Depois do DELETE por ID:')

deletar_por_cidade('Curitiba')
mostrar_alunos('Depois do DELETE por Cidade:')
