from bd import conectar, desconectar

def inserir_vendedor(nome, causa_social, tipo, nota_media, cargo_id):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = """
        INSERT INTO Vendedor (nome, causa_social, tipo, nota_media, cargo_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nome, causa_social, tipo, nota_media, cargo_id)
        cursor.execute(sql, valores)
        conn.commit()
        print("Vendedor inserido com ID:", cursor.lastrowid)
        cursor.close()
        desconectar(conn)

def listar_vendedores():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = """
        SELECT v.id, v.nome, v.causa_social, v.tipo, v.nota_media, c.nome
        FROM Vendedor v
        LEFT JOIN Cargo c ON v.cargo_id = c.id
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for row in resultados:
            print(f"ID: {row[0]}, Nome: {row[1]}, Causa Social: {row[2]}, Tipo: {row[3]}, Nota Média: {row[4]}, Cargo: {row[5]}")
        cursor.close()
        desconectar(conn)

def buscar_vendedor_por_id(id):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = """
        SELECT v.id, v.nome, v.causa_social, v.tipo, v.nota_media, c.nome
        FROM Vendedor v
        LEFT JOIN Cargo c ON v.cargo_id = c.id
        WHERE v.id = %s
        """
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            print(f"ID: {resultado[0]}, Nome: {resultado[1]}, Causa Social: {resultado[2]}, Tipo: {resultado[3]}, Nota Média: {resultado[4]}, Cargo: {resultado[5]}")
        else:
            print("Vendedor não encontrado.")
        cursor.close()
        desconectar(conn)
