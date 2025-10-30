from db import conectar, desconectar

def inserir_transportadora(nome, cidade):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO transportadoras (nome, cidade) VALUES (%s, %s)"
    cursor.execute(sql, (nome, cidade))
    conn.commit()
    print("Transportadora cadastrada com sucesso!")
    cursor.close()
    desconectar(conn)

def listar_transportadoras():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transportadoras")
    transportadoras = cursor.fetchall()
    if transportadoras:
        print("\n--- Lista de Transportadoras ---")
        for t in transportadoras:
            print(f"ID: {t[0]} | Nome: {t[1]} | Cidade: {t[2]}")
    else:
        print("Nenhuma transportadora cadastrada.")
    cursor.close()
    desconectar(conn)

def atualizar_transportadora(id, novo_nome, nova_cidade):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE transportadoras SET nome = %s, cidade = %s WHERE id = %s"
    cursor.execute(sql, (novo_nome, nova_cidade, id))
    conn.commit()
    if cursor.rowcount > 0:
        print("Transportadora atualizada com sucesso!")
    else:
        print("Transportadora não encontrada.")
    cursor.close()
    desconectar(conn)

def remover_transportadora(id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM transportadoras WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Transportadora removida com sucesso!")
    else:
        print("Transportadora não encontrada.")
    cursor.close()
    desconectar(conn)
a
