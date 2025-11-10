from db import conectar, desconectar


def inserir_transportadora(nome, cidade):
    conn = conectar()
    cursor = conn.cursor()
    try:
        sql = """
            INSERT INTO transportadoras (nome, cidade)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (nome, cidade))
        conn.commit()
        print("Transportadora cadastrada com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar transportadora:", e)
        conn.rollback()
    finally:
        cursor.close()
        desconectar(conn)


def listar_transportadoras():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, nome, cidade FROM transportadoras ORDER BY id")
        transportadoras = cursor.fetchall()

        if transportadoras:
            print("\n--- Lista de Transportadoras ---")
            for t in transportadoras:
                print(f"ID: {t[0]} | Nome: {t[1]} | Cidade: {t[2]}")
        else:
            print("Nenhuma transportadora cadastrada.")
    except Exception as e:
        print("Erro ao listar transportadoras:", e)
    finally:
        cursor.close()
        desconectar(conn)


def atualizar_transportadora(id, novo_nome, nova_cidade):
    conn = conectar()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE transportadoras
            SET nome = %s, cidade = %s
            WHERE id = %s
        """
        cursor.execute(sql, (novo_nome, nova_cidade, id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Transportadora atualizada com sucesso!")
        else:
            print("Transportadora não encontrada.")
    except Exception as e:
        print("Erro ao atualizar transportadora:", e)
        conn.rollback()
    finally:
        cursor.close()
        desconectar(conn)


def remover_transportadora(id):
    conn = conectar()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM transportadoras WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Transportadora removida com sucesso!")
        else:
            print("Transportadora não encontrada.")
    except Exception as e:
        print("Erro ao remover transportadora:", e)
        conn.rollback()
    finally:
        cursor.close()
        desconectar(conn)
