from bd import conectar, desconectar

def definir_cargo_ativo(cargo, usuario):
    """
    Define o cargo ativo de um usuário no banco.
    Atualiza se já existir, ou insere se for novo.
    """
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        try:
            sql_update = "UPDATE Cargo_Ativo SET cargo_nome = %s, data_login = NOW() WHERE usuario = %s"
            cursor.execute(sql_update, (cargo, usuario))

            if cursor.rowcount == 0:
                sql_insert = "INSERT INTO Cargo_Ativo (cargo_nome, usuario) VALUES (%s, %s)"
                cursor.execute(sql_insert, (cargo, usuario))

            conn.commit()
            print(f"[OK] Cargo ativo definido para {cargo} (usuário {usuario})")
        except Exception as e:
            print("[ERRO] Não foi possível definir cargo ativo:", e)
        finally:
            cursor.close()
            desconectar(conn)
