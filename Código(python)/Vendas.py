from bd import conectar, desconectar

def _estoque_suficiente(cur, produto_id, quantidade):
    cur.execute("SELECT quantidade_em_estoque FROM Produtos WHERE id = %s", (produto_id,))
    r = cur.fetchone()
    if not r:
        raise ValueError(f"Produto {produto_id} não encontrado.")
    return r[0] >= quantidade

def criar_venda(cliente_id, transportadora_id, endereco_des, valor_transp, itens):
    if not itens:
        raise ValueError("A venda precisa ter ao menos um produto.")
    conn = conectar()
    try:
        cur = conn.cursor()
        for prod_id, qtd in itens:
            if not _estoque_suficiente(cur, prod_id, qtd):
                raise ValueError(f"Estoque insuficiente para o produto {prod_id}.")
        cur.execute("""
            INSERT INTO Venda (cliente_id, transportadora_id, endereco_des, valor_transp)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, transportadora_id, endereco_des, valor_transp))
        venda_id = cur.lastrowid
        for prod_id, qtd in itens:
            cur.execute("""
                INSERT INTO venda_produtos (venda_id, produto_id, quantidade)
                VALUES (%s, %s, %s)
            """, (venda_id, prod_id, qtd))
        cur.execute("""
            SELECT SUM(p.valor * vp.quantidade)
            FROM venda_produtos vp
            JOIN Produtos p ON p.id = vp.produto_id
            WHERE vp.venda_id = %s
        """, (venda_id,))
        total_produtos = cur.fetchone()[0] or 0
        conn.commit()
        print(f"✅ Venda criada (ID: {venda_id}) | Total produtos: {total_produtos:.2f} | Frete: {valor_transp:.2f}")
        try:
            cur.callproc('aplicar_cashback', (cliente_id, float(total_produtos)))
            conn.commit()
        except Exception:
            pass
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
                   COALESCE(SUM(p.valor * vp.quantidade), 0) AS total_produtos
            FROM Venda v
            LEFT JOIN venda_produtos vp ON vp.venda_id = v.id
            LEFT JOIN Produtos p ON p.id = vp.produto_id
            GROUP BY v.id
            ORDER BY v.id DESC
        """)
        vendas = cur.fetchall()
        if not vendas:
            print("Nenhuma venda encontrada.")
            return
        print("\n--- Lista de Vendas ---")
        for v in vendas:
            total_geral = (v[6] or 0) + float(v[5] or 0)
            print(f"ID:{v[0]} | Cliente:{v[1]} | Transp:{v[2]} | Total Geral: R$ {total_geral:.2f}")
    finally:
        cur.close()
        desconectar(conn)

def detalhes_venda(venda_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, cliente_id, transportadora_id, data_hora, endereco_des, valor_transp
            FROM Venda WHERE id = %s
        """, (venda_id,))
        v = cur.fetchone()
        if not v:
            print("Venda não encontrada.")
            return
        cur.execute("""
            SELECT vp.produto_id, p.nome, vp.quantidade, p.valor, (vp.quantidade * p.valor) AS subtotal
            FROM venda_produtos vp
            JOIN Produtos p ON p.id = vp.produto_id
            WHERE vp.venda_id = %s
        """, (venda_id,))
        itens = cur.fetchall()
        print(f"\nVenda {v[0]} | Cliente:{v[1]} | Transp:{v[2]} | Data:{v[3]} | Frete:R$ {v[5]:.2f}")
        total = 0
        for i in itens:
            print(f"- Produto {i[0]} ({i[1]}): {i[2]}x R${i[3]:.2f} = R${i[4]:.2f}")
            total += float(i[4])
        print(f"Total produtos: R$ {total:.2f} | Total geral: R$ {total + float(v[5]):.2f}")
    finally:
        cur.close()
        desconectar(conn)

def remover_venda(venda_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM venda_produtos WHERE venda_id = %s", (venda_id,))
        cur.execute("DELETE FROM Venda WHERE id = %s", (venda_id,))
        conn.commit()
        if cur.rowcount:
            print("🗑️ Venda removida com sucesso.")
        else:
            print("Venda não encontrada.")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao remover venda: {e}")
    finally:
        cur.close()
        desconectar(conn)
