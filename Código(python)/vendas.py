from bd import conectar, desconectar

def criar_venda(cliente_id, transportadora_id, endereco_des, valor_transp, itens):
    conn = conectar()
    try:
        cur = conn.cursor()
        if not itens:
            raise ValueError("A venda precisa ter ao menos um produto.")

        # Inserção da venda
        cur.execute("""
            INSERT INTO Venda (cliente_id, transportadora_id, endereco_des, valor_transp)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, transportadora_id, endereco_des, valor_transp))
        venda_id = cur.lastrowid

        # Inserção dos produtos da venda
        for pid, qtd in itens:
            cur.execute("""
                INSERT INTO venda_produtos (venda_id, produto_id, quantidade)
                VALUES (%s, %s, %s)
            """, (venda_id, pid, qtd))

        conn.commit()
        print(f"✅ Venda criada (ID: {venda_id}) com {len(itens)} produto(s).")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao criar venda: {e}")
    finally:
        cur.close()
        desconectar(conn)

def listar_vendas():
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT v.id, v.cliente_id, v.transportadora_id, v.data_hora, v.endereco_des, v.valor_transp,
                   COALESCE(SUM(p.valor * vp.quantidade), 0)
            FROM Venda v
            LEFT JOIN venda_produtos vp ON v.id = vp.venda_id
            LEFT JOIN Produtos p ON p.id = vp.produto_id
            GROUP BY v.id ORDER BY v.id DESC
        """)
        vendas = cur.fetchall()
        if not vendas:
            print("Nenhuma venda encontrada.")
            return
        print("\n--- LISTA DE VENDAS ---")
        for v in vendas:
            total = (v[6] or 0) + float(v[5] or 0)
            print(f"ID:{v[0]} | Cliente:{v[1]} | Transp:{v[2]} | Total:R${total:.2f}")
    finally:
        cur.close()
        desconectar(conn)

def menu_vendas():
    while True:
        print("\n--- VENDAS ---")
        print("1) Criar venda")
        print("2) Listar vendas")
        print("0) Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                cid = int(input("ID do cliente: "))
                tid = int(input("ID da transportadora: "))
                end = input("Endereço de destino: ")
                frete = float(input("Valor do frete: "))
                itens = []
                while True:
                    s = input("Produto ID (vazio para encerrar): ").strip()
                    if not s:
                        break
                    pid = int(s)
                    qtd = int(input("Quantidade: "))
                    itens.append((pid, qtd))
                criar_venda(cid, tid, end, frete, itens)
            elif op == "2":
                listar_vendas()
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"⚠️ Erro: {e}")
