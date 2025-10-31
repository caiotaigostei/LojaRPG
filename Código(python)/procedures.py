from db import conectar, desconectar

def criar_procedures_e_triggers():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("USE Loja_RPG;")

    # Procedure: aplicar cashback para clientes especiais
    cursor.execute("""
    CREATE PROCEDURE IF NOT EXISTS aplicar_cashback(IN cliente_id INT, IN valor_compra DECIMAL(10,2))
    BEGIN
        DECLARE cashback_valor DECIMAL(10,2);
        SELECT cashback INTO cashback_valor FROM clientes_especiais WHERE cliente_id = cliente_id;
        IF cashback_valor IS NOT NULL THEN
            UPDATE clientes_especiais
            SET cashback = cashback + (valor_compra * 0.05)
            WHERE cliente_id = cliente_id;
        END IF;
    END;
    """)

    # Procedure: atualizar nota média do vendedor
    cursor.execute("""
    CREATE PROCEDURE IF NOT EXISTS atualizar_nota_vendedor(IN vendedor INT, IN nova_nota DECIMAL(3,1))
    BEGIN
        DECLARE media DECIMAL(3,1);
        SELECT AVG(nova_nota) INTO media;
        UPDATE Vendedor SET nota_media = media WHERE id = vendedor;
    END;
    """)

    # Trigger: reduzir estoque quando ocorre uma venda
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS trg_reduzir_estoque
    AFTER INSERT ON venda_produtos
    FOR EACH ROW
    BEGIN
        UPDATE Produtos
        SET quantidade_em_estoque = quantidade_em_estoque - NEW.quantidade
        WHERE id = NEW.produto_id;
    END;
    """)

    # Trigger: restaurar estoque se venda for removida
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS trg_restaurar_estoque
    AFTER DELETE ON venda_produtos
    FOR EACH ROW
    BEGIN
        UPDATE Produtos
        SET quantidade_em_estoque = quantidade_em_estoque + OLD.quantidade
        WHERE id = OLD.produto_id;
    END;
    """)

    # Trigger: registrar cashback automático após venda
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS trg_cashback_venda
    AFTER INSERT ON Venda
    FOR EACH ROW
    BEGIN
        CALL aplicar_cashback(NEW.cliente_id, (
            SELECT SUM(p.valor * vp.quantidade)
            FROM venda_produtos vp
            JOIN Produtos p ON vp.produto_id = p.id
            WHERE vp.venda_id = NEW.id
        ));
    END;
    """)

    print("✅ Procedures e Triggers criados com sucesso!")
    cursor.close()
    desconectar(conn)

if _name_ == "_main_":
    criar_procedures_e_triggers()
