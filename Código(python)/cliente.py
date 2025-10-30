from db import conectar, desconectar

def inserir_cliente(id, nome, idade, sexo, data_nasc):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO Cliente (id, nome, idade, sexo, data_nascimento) VALUES (%s, %s, %s, %s, %s)"
        valores = (id, nome, idade, sexo, data_nasc)
        cursor.execute(sql, valores)
        conn.commit()
        print(cursor.rowcount, "cliente(s) inserido(s).")
        cursor.close()
        desconectar(conn)

def listar_clientes():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM Cliente"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for row in resultados:
            print("ID:", row[0], "Nome:", row[1], "Idade:", row[2], "Sexo:", row[3], "Data de Nascimento:", row[4])
        cursor.close()
        desconectar(conn)

def buscar_cliente_por_id(id):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM Cliente WHERE id = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            print("ID:", resultado[0], "Nome:", resultado[1], "Idade:", resultado[2], "Sexo:", resultado[3], "Data de Nascimento:", resultado[4])
        else:
            print("Cliente nao encontrado.")
        cursor.close()
        desconectar(conn)

def inserir_cliente_especial(cliente_id, cashback):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO clientes_especiais (cliente_id, cashback) VALUES (%s, %s)"
        cursor.execute(sql, (cliente_id, cashback))
        conn.commit()
        print(cursor.rowcount, "cliente especial inserido(s).")
        cursor.close()
        desconectar(conn)

def listar_clientes_especiais():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT c.id, c.nome, c.idade, c.sexo, c.data_nascimento, ce.cashback FROM Cliente c JOIN clientes_especiais ce ON c.id = ce.cliente_id"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for row in resultados:
            print("ID:", row[0], "Nome:", row[1], "Idade:", row[2], "Sexo:", row[3], "Data de Nascimento:", row[4], "Cashback:", row[5])
        cursor.close()
        desconectar(conn)

def atualizar_cashback(cliente_id, novo_cashback):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE clientes_especiais SET cashback = %s WHERE cliente_id = %s"
        cursor.execute(sql, (novo_cashback, cliente_id))
        conn.commit()
        print(cursor.rowcount, "cliente(s) atualizado(s).")
        cursor.close()
        desconectar(conn)
        if novo_cashback <= 0:
            remover_cliente_especial(cliente_id)

def remover_cliente_especial(cliente_id):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM clientes_especiais WHERE cliente_id = %s"
        cursor.execute(sql, (cliente_id,))
        conn.commit()
        print(cursor.rowcount, "cliente especial removido(s).")
        cursor.close()
        desconectar(conn)
