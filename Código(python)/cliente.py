from bd import conectar, desconectar

def inserir_cliente(nome, idade, sexo, data_nasc):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO Cliente (nome, idade, sexo, data_nascimento) VALUES (%s, %s, %s, %s)"
        valores = (nome, idade, sexo, data_nasc)
        try:
            cursor.execute(sql, valores)
            conn.commit()
            print("Cliente inserido com sucesso! ID:", cursor.lastrowid)
        except Exception as e:
            print("Erro ao inserir cliente:", e)
        finally:
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
            print("ID:", row[0], "Nome:", row[1], "Idade:", row[2],
                  "Sexo:", row[3], "Data de Nascimento:", row[4])
        cursor.close()
        desconectar(conn)

def buscar_cliente_por_id(cliente_id):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM Cliente WHERE id = %s"
        cursor.execute(sql, (cliente_id,))
        resultado = cursor.fetchone()
        if resultado:
            print("ID:", resultado[0], "Nome:", resultado[1], "Idade:", resultado[2],
                  "Sexo:", resultado[3], "Data de Nascimento:", resultado[4])
        else:
            print("Cliente não encontrado.")
        cursor.close()
        desconectar(conn)

def inserir_cliente_especial(cliente_id, cashback):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO clientes_especiais (cliente_id, cashback) VALUES (%s, %s)"
        try:
            cursor.execute(sql, (cliente_id, cashback))
            conn.commit()
            print("Cliente especial inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir cliente especial:", e)
        finally:
            cursor.close()
            desconectar(conn)

def listar_clientes_especiais():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = """
        SELECT c.id, c.nome, c.idade, c.sexo, c.data_nascimento, ce.cashback
        FROM Cliente c
        JOIN clientes_especiais ce ON c.id = ce.cliente_id
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for row in resultados:
            print("ID:", row[0], "Nome:", row[1], "Idade:", row[2],
                  "Sexo:", row[3], "Data de Nascimento:", row[4],
                  "Cashback:", row[5])
        cursor.close()
        desconectar(conn)

def atualizar_cashback(cliente_id, novo_cashback):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE clientes_especiais SET cashback = %s WHERE cliente_id = %s"
        try:
            cursor.execute(sql, (novo_cashback, cliente_id))
            conn.commit()
            print("Cashback atualizado com sucesso!")
            if novo_cashback <= 0:
                remover_cliente_especial(cliente_id)
        except Exception as e:
            print("Erro ao atualizar cashback:", e)
        finally:
            cursor.close()
            desconectar(conn)

def remover_cliente_especial(cliente_id):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM clientes_especiais WHERE cliente_id = %s"
        try:
            cursor.execute(sql, (cliente_id,))
            conn.commit()
            print("Cliente especial removido com sucesso!")
        except Exception as e:
            print("Erro ao remover cliente especial:", e)
        finally:
            cursor.close()
            desconectar(conn)

def ranking_clientes_especiais():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = """
        SELECT c.id, c.nome, c.idade, c.sexo, c.data_nascimento, ce.cashback
        FROM Cliente c
        JOIN clientes_especiais ce ON c.id = ce.cliente_id
        ORDER BY ce.cashback DESC
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("\n--- Ranking de Clientes Especiais por Cashback ---")
        for i, row in enumerate(resultados, start=1):
            print(f"{i}º - ID: {row[0]}, Nome: {row[1]}, Cashback: {row[5]}")
        cursor.close()
        desconectar(conn)
