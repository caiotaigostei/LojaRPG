from bd import conectar, desconectar

def inserir_produto(nome, descricao, quantidade_em_estoque, valor, observacoes, vendedor_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        sql = """
            INSERT INTO Produtos (nome, descricao, quantidade_em_estoque, valor, observacoes, vendedor_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, (nome, descricao, quantidade_em_estoque, valor, observacoes, vendedor_id))
        conn.commit()
        print(f"✅ Produto inserido com sucesso (ID: {cur.lastrowid})")
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
            print(f"ID:{p[0]} | Nome:{p[1]} | Desc:{p[2]} | Estoque:{p[3]} | Valor:{p[4]} | Obs:{p[5]} | Vendedor:{p[6]}")
        else:
            print("Produto não encontrado.")
    finally:
        cur.close()
        desconectar(conn)

def atualizar_produto(produto_id, nome=None, descricao=None, quantidade_em_estoque=None, valor=None, observacoes=None, vendedor_id=None):
    campos, valores = [], []
    if nome is not None:
        campos.append("nome = %s"); valores.append(nome)
    if descricao is not None:
        campos.append("descricao = %s"); valores.append(descricao)
    if quantidade_em_estoque is not None:
        campos.append("quantidade_em_estoque = %s"); valores.append(quantidade_em_estoque)
    if valor is not None:
        campos.append("valor = %s"); valores.append(valor)
    if observacoes is not None:
        campos.append("observacoes = %s"); valores.append(observacoes)
    if vendedor_id is not None:
        campos.append("vendedor_id = %s"); valores.append(vendedor_id)
    if not campos:
        print("Nenhuma alteração informada.")
        return
    valores.append(produto_id)
    conn = conectar()
    try:
        cur = conn.cursor()
        sql = f"UPDATE Produtos SET {', '.join(campos)} WHERE id = %s"
        cur.execute(sql, tuple(valores))
        conn.commit()
        if cur.rowcount:
            print("✅ Produto atualizado.")
        else:
            print("Produto não encontrado.")
    finally:
        cur.close()
        desconectar(conn)

def remover_produto(produto_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM Produtos WHERE id = %s", (produto_id,))
        conn.commit()
        if cur.rowcount:
            print("🗑️ Produto removido com sucesso.")
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
        if cur.rowcount:
            print("✅ Estoque atualizado.")
        else:
            print("Produto não encontrado.")
    finally:
        cur.close()
        desconectar(conn)

def listar_produtos_por_vendedor(vendedor_id):
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nome, quantidade_em_estoque, valor
            FROM Produtos WHERE vendedor_id = %s
        """, (vendedor_id,))
        produtos = cur.fetchall()
        if not produtos:
            print("Nenhum produto vinculado a este vendedor.")
            return
        for p in produtos:
            print(f"ID:{p[0]} | Nome:{p[1]} | Estoque:{p[2]} | Valor:{p[3]}")
    finally:
        cur.close()
        desconectar(conn)
