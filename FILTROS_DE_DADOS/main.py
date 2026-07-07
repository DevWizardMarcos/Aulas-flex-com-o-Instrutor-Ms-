import sqlite3

# criando a conexao com o banco de dados (em memoria)
# :memory: quer dizer que o banco existe so enquanto o programa esta rodando.
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


def mostrar_resultado(titulo, resultado):
    """Funcao simples para organizar a saida dos filtros."""
    print('=' * 90)
    print(titulo)
    print(resultado)


# Criando a Tabela como Exemplo
# PRIMARY KEY identifica cada produto de forma unica.
cursor.execute('''
    CREATE TABLE Produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL,
        categoria TEXT,
        estoque INTEGER
    )
''')

# Inserindo dados na tabela Produtos.
# Aqui colocamos mais produtos para testar melhor os filtros do slide.
produtos = [
    (1, 'Monitor', 800.00, 'Informatica', 10),
    (2, 'Mouse', 50.00, 'Informatica', 35),
    (3, 'Teclado', 150.00, 'Informatica', 20),
    (4, 'Cadeira', 350.00, 'Moveis', 7),
    (5, 'Fone', 90.00, 'Audio', 15),
    (6, 'Webcam', 220.00, 'Informatica', 5),
]

cursor.executemany('''
    INSERT INTO Produtos (id, nome, preco, categoria, estoque)
    VALUES (?, ?, ?, ?, ?)
''', produtos)

# Salva as insercoes feitas no banco.
conn.commit()

# =============================== PRIMEIRA PARTE ===============================

# Exemplo de SELECT sem WHERE.
# Sem filtro ele retorna todos os registros escolhidos.
cursor.execute('SELECT nome FROM Produtos')
mostrar_resultado('Sem filtros:', cursor.fetchall())

# Operador de igualdade (=).
# Busca exatamente o produto que tem preco igual a 50.
cursor.execute('SELECT nome, preco FROM Produtos WHERE preco = 50.00')
mostrar_resultado('Preco = 50:', cursor.fetchall())

# Operador de maior (>).
# Busca produtos com preco maior que 100.
cursor.execute('SELECT nome, preco FROM Produtos WHERE preco > 100.00')
mostrar_resultado('Preco maior que 100:', cursor.fetchall())

# Operador de menor (<).
# Busca produtos com preco menor que 100.
cursor.execute('SELECT nome, preco FROM Produtos WHERE preco < 100.00')
mostrar_resultado('Preco menor que 100:', cursor.fetchall())

# Operador de diferente (<>).
# Busca todos os produtos, menos o Mouse.
cursor.execute('SELECT nome, preco FROM Produtos WHERE nome <> "Mouse"')
mostrar_resultado('Nome diferente de Mouse:', cursor.fetchall())

# =============================== SEGUNDA PARTE ================================

# Usando o AND.
# As duas condicoes precisam ser verdadeiras ao mesmo tempo.
cursor.execute('''
    SELECT nome, preco
    FROM Produtos
    WHERE preco > 100 AND preco < 300
''')
mostrar_resultado('Preco maior que 100 E menor que 300:', cursor.fetchall())

# Usando o OR.
# Retorna quando pelo menos uma das condicoes for verdadeira.
cursor.execute('''
    SELECT nome, preco, estoque
    FROM Produtos
    WHERE preco > 500 OR estoque < 10
''')
mostrar_resultado('Preco maior que 500 OU estoque menor que 10:', cursor.fetchall())

# Usando o NOT IN.
# Retorna produtos que nao estao dentro da lista informada.
cursor.execute('''
    SELECT nome
    FROM Produtos
    WHERE nome NOT IN ("Monitor", "Mouse")
''')
mostrar_resultado('Produtos que nao sao Monitor nem Mouse:', cursor.fetchall())

# Usando o IN.
# Retorna somente os produtos que estao dentro da lista informada.
cursor.execute('''
    SELECT nome, categoria
    FROM Produtos
    WHERE categoria IN ("Audio", "Moveis")
''')
mostrar_resultado('Produtos das categorias Audio ou Moveis:', cursor.fetchall())

# Usando o BETWEEN.
# BETWEEN filtra valores dentro de um intervalo, incluindo os limites.
cursor.execute('''
    SELECT nome, preco
    FROM Produtos
    WHERE preco BETWEEN 90 AND 350
''')
mostrar_resultado('Preco entre 90 e 350:', cursor.fetchall())

# Usando o LIKE.
# LIKE procura um padrao dentro do texto.
# O simbolo % significa "qualquer quantidade de caracteres".
cursor.execute('''
    SELECT nome
    FROM Produtos
    WHERE nome LIKE "M%"
''')
mostrar_resultado('Produtos que comecam com a letra M:', cursor.fetchall())

# Usando ORDER BY.
# ORDER BY organiza o resultado. ASC = crescente, DESC = decrescente.
cursor.execute('''
    SELECT nome, preco
    FROM Produtos
    ORDER BY preco DESC
''')
mostrar_resultado('Produtos ordenados pelo maior preco:', cursor.fetchall())

# =================== PRIMEIRA INTEGRACAO COM PYTHON ===================

# Criando uma funcao em Python para consultar o banco.
# O ponto de interrogacao (?) deixa a consulta mais segura e reaproveitavel.
def buscar_produtos_por_preco(preco_minimo):
    cursor.execute('''
        SELECT nome, preco
        FROM Produtos
        WHERE preco >= ?
        ORDER BY preco
    ''', (preco_minimo,))
    return cursor.fetchall()


# Chamando a funcao Python e passando o valor minimo como parametro.
resultado_python = buscar_produtos_por_preco(150)
mostrar_resultado('Consulta feita por uma funcao Python, preco >= 150:', resultado_python)

# Fechando a conexao com o banco no final do programa.
conn.close()
