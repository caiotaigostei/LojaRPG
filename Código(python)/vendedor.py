from db import conectar, desconectar

def inserir_vendedor(id, nome, causa_social, tipo, nota_media):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO Vendedor (id, nome, causa_social, tipo, nota_media) VALUES (%s, %s, %s, %s, %s)"
        valores = (id, nome, causa_social, tipo, nota_media)
        cursor.execute(sql, valores)
        conn.commit()
        print(cursor.rowcount, "vendedor(es) inserido(s).")
        cursor.close()
        desconectar(conn)

def listar_vendedores():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM Vendedor"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for row in resultados:
            print("ID:", row[0], "Nome:", row[1], "Causa Social:", row[2], "Tipo:", row[3], "Nota Média:", row[4])
        cursor.close()
        desconectar(conn)

def buscar_vendedor_por_id(id):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM Vendedor WHERE id = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            print("ID:", resultado[0], "Nome:", resultado[1], "Causa Social:", resultado[2], "Tipo:", resultado[3], "Nota Média:", resultado[4])
        else:
            print("Vendedor nao encontrado.")
        cursor.close()
        desconectar(conn)




