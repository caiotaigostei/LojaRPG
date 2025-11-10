from db import conectar, desconectar

def criar_procedures_e_triggers():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("USE Loja_RPG;")

    cursor.execute("DROP PROCEDURE IF EXISTS aplicar_cashback;")
    cursor.execute("""
    CREATE PROCEDURE aplicar_cashback(IN p_cliente_id INT, IN p_valor_compra DECIMAL(10,2))
    BEGIN
        DECLARE v_cashback DECIMAL(10,2);
        SELECT cashback INTO v_cashback
        FROM clientes_especiais
        WHERE cliente_id = p_cliente_id;
        IF v_cashback IS NOT NULL THEN
            UPDATE clientes_especiais
            SET cashback = cashback + (p_valor_compra * 0.05)
            WHERE cliente_id = p_cliente_id;
        END IF;
    END;
    """)

    cursor.execute("DROP PROCEDURE IF EXISTS atualizar_nota_vendedor;")
    cursor.execute("""
    CREATE PROCEDURE atualizar_nota_vendedor(IN p_vendedor_id INT, IN p_nova_nota DECIMAL(3,1))
    BEGIN
        DECLARE v_media DECIMAL(3,1);
        SELECT ROUND(AVG(p_nova_nota),1) INTO v_media;
        UPDATE Vendedor
        SET nota_media = v_media
        WHERE id = p_vendedor_id;
    END;
    """)

    cursor.execute("DROP TRIGGER IF EXISTS trg_reduzir_estoque;")
    cursor.execute("""
    CREATE TRIGGER trg_reduzir_estoque
    AFTER INSERT ON venda_produtos
    FOR EACH ROW
    BEGIN
        UPDATE Produtos
        SET quantidade_em_estoque = quantidade_em_estoque - NEW.quantidade
        WHERE id = NEW.produto_id;
    END;
    """)

    cursor.execute("DROP TRIGGER IF EXISTS trg_restaurar_estoque;")
    cursor.execute("""
    CREATE TRIGGER trg_restaurar_estoque
    AFTER DELETE ON venda_produtos
    FOR EACH ROW
    BEGIN
        UPDATE Produtos
        SET quantidade_em_estoque = quantidade_em_estoque + OLD.quantidade
        WHERE id = OLD.produto_id;
    END;
    """)

    cursor.execute("DROP TRIGGER IF EXISTS trg_cashback_venda;")
    cursor.execute("""
    CREATE TRIGGER trg_cashback_venda
    AFTER INSERT ON Venda
    FOR EACH ROW
    BEGIN
        DECLARE v_total_compra DECIMAL(10,2);
        SELECT SUM(p.valor * vp.quantidade)
        INTO v_total_compra
        FROM venda_produtos vp
        JOIN Produtos p ON vp.produto_id = p.id
        WHERE vp.venda_id = NEW.id;
        IF v_total_compra IS NOT NULL THEN
            CALL aplicar_cashback(NEW.cliente_id, v_total_compra);
        END IF;
    END;
    """)

    conn.commit()
    cursor.close()
    desconectar(conn)


if __name__ == "__main__":
    criar_procedures_e_triggers()
