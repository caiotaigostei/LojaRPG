from bd import conectar, desconectar

def inserir_vendedor(nome, causa_social, tipo, nota_media, cargo_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO Vendedor (nome, causa_social, tipo, nota_media, cargo_id)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (nome, causa_social, tipo, nota_media, cargo_id)
    try:
        cursor.execute(sql, valores)
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        desconectar(conn)

def listar_vendedores():
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        SELECT v.id, v.nome, v.causa_social, v.tipo, v.nota_media, c.nome
        FROM Vendedor v
        LEFT JOIN Cargo c ON v.cargo_id = c.id
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    desconectar(conn)
    return resultados

def buscar_vendedor_por_id(vendedor_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        SELECT v.id, v.nome, v.causa_social, v.tipo, v.nota_media, c.nome
        FROM Vendedor v
        LEFT JOIN Cargo c ON v.cargo_id = c.id
        WHERE v.id = %s
    """
    cursor.execute(sql, (vendedor_id,))
    resultado = cursor.fetchone()
    cursor.close()
    desconectar(conn)
    return resultado
