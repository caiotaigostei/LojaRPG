from bd import conectar, desconectar

def inserir_cliente(nome, idade, sexo, data_nasc):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Cliente (nome, idade, sexo, data_nascimento) VALUES (%s, %s, %s, %s)"
    valores = (nome, idade, sexo, data_nasc)
    try:
        cursor.execute(sql, valores)
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        desconectar(conn)

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT * FROM Cliente"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    desconectar(conn)
    return resultados

def buscar_cliente_por_id(cliente_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT * FROM Cliente WHERE id = %s"
    cursor.execute(sql, (cliente_id,))
    resultado = cursor.fetchone()
    cursor.close()
    desconectar(conn)
    return resultado

def inserir_cliente_especial(cliente_id, cashback):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO clientes_especiais (cliente_id, cashback) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (cliente_id, cashback))
        conn.commit()
    finally:
        cursor.close()
        desconectar(conn)

def listar_clientes_especiais():
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        SELECT c.id, c.nome, c.idade, c.sexo, c.data_nascimento, ce.cashback
        FROM Cliente c
        JOIN clientes_especiais ce ON c.id = ce.cliente_id
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    desconectar(conn)
    return resultados

def atualizar_cashback(cliente_id, novo_cashback):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE clientes_especiais SET cashback = %s WHERE cliente_id = %s"
    try:
        cursor.execute(sql, (novo_cashback, cliente_id))
        conn.commit()
        if novo_cashback <= 0:
            remover_cliente_especial(cliente_id)
    finally:
        cursor.close()
        desconectar(conn)

def remover_cliente_especial(cliente_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM clientes_especiais WHERE cliente_id = %s"
    try:
        cursor.execute(sql, (cliente_id,))
        conn.commit()
    finally:
        cursor.close()
        desconectar(conn)
