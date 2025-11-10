from bd import conectar, desconectar

def inserir_transportadora(nome, cidade):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO transportadoras (nome, cidade) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (nome, cidade))
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        desconectar(conn)

def listar_transportadoras():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, nome, cidade FROM transportadoras ORDER BY id")
        return cursor.fetchall()
    finally:
        cursor.close()
        desconectar(conn)

def atualizar_transportadora(transportadora_id, novo_nome, nova_cidade):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE transportadoras SET nome = %s, cidade = %s WHERE id = %s"
    try:
        cursor.execute(sql, (novo_nome, nova_cidade, transportadora_id))
        conn.commit()
        return cursor.rowcount  # retorna quantas linhas foram afetadas
    finally:
        cursor.close()
        desconectar(conn)

def remover_transportadora(transportadora_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM transportadoras WHERE id = %s"
    try:
        cursor.execute(sql, (transportadora_id,))
        conn.commit()
        return cursor.rowcount  # retorna quantas linhas foram removidas
    finally:
        cursor.close()
        desconectar(conn)
