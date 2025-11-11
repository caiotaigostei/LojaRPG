from bd import conectar, desconectar

def inserir_produto(nome, descricao, quantidade_em_estoque, valor, observacoes, vendedor_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Produtos (nome, descricao, quantidade_em_estoque, valor, observacoes, vendedor_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nome, descricao, quantidade_em_estoque, valor, observacoes, vendedor_id))
        conn.commit()
        print(f"✅ Produto inserido com sucesso (ID: {cur.lastrowid})")
    except Exception as e:
        print(f"❌ Erro ao inserir produto: {e}")
    finally:
        cur.close()
        desconectar(conn)

def listar_produtos():
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nome, descricao, quantidade_em_estoque, valor, vendedor_id
            FROM Produtos ORDER BY id
        """)
        produtos = cur.fetchall()
        if not produtos:
            print("Nenhum produto encontrado.")
            return
        print("\n--- Lista de Produtos ---")
        for p in produtos:
            print(f"ID:{p[0]} | Nome:{p[1]} | Estoque:{p[3]} | Valor:{p[4]} | Vendedor:{p[5]}")
    finally:
        cur.close()
        desconectar(conn)

def buscar_produto_por_id(produto_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nome, descricao, quantidade_em_estoque, valor, observacoes, vendedor_id
            FROM Produtos WHERE id = %s
        """, (produto_id,))
        p = cur.fetchone()
        if p:
            print(f"ID:{p[0]} | Nome:{p[1]} | Estoque:{p[3]} | Valor:{p[4]} | Obs:{p[5]} | Vendedor:{p[6]}")
        else:
            print("Produto não encontrado.")
    finally:
        cur.close()
        desconectar(conn)

def atualizar_estoque(produto_id, nova_qtd):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("UPDATE Produtos SET quantidade_em_estoque = %s WHERE id = %s", (nova_qtd, produto_id))
        conn.commit()
        print("✅ Estoque atualizado.")
    except Exception as e:
        print(f"❌ Erro ao atualizar estoque: {e}")
    finally:
        cur.close()
        desconectar(conn)

def remover_produto(produto_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM Produtos WHERE id = %s", (produto_id,))
        conn.commit()
        print("🗑️ Produto removido com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao remover produto: {e}")
    finally:
        cur.close()
        desconectar(conn)

def menu_produtos():
    while True:
        print("\n--- PRODUTOS ---")
        print("1) Inserir produto")
        print("2) Listar produtos")
        print("3) Buscar produto por ID")
        print("4) Atualizar estoque")
        print("5) Remover produto")
        print("0) Voltar")
        op = input("Escolha: ").strip()

        try:
            if op == "1":
                nome = input("Nome: ")
                desc = input("Descrição: ")
                estq = int(input("Estoque: "))
                val = float(input("Valor: "))
                obs = input("Observações: ")
                vend = int(input("ID do vendedor: "))
                inserir_produto(nome, desc, estq, val, obs, vend)
            elif op == "2":
                listar_produtos()
            elif op == "3":
                _id = int(input("ID do produto: "))
                buscar_produto_por_id(_id)
            elif op == "4":
                _id = int(input("ID do produto: "))
                nova_qtd = int(input("Nova quantidade: "))
                atualizar_estoque(_id, nova_qtd)
            elif op == "5":
                _id = int(input("ID do produto: "))
                remover_produto(_id)
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"⚠️ Erro: {e}")
