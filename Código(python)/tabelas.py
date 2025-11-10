from db import conectar, desconectar

def criar_tabelas():
    try:
        conn = conectar()
        cursor = conn.cursor()

        # --- Criação do banco e uso ---
        cursor.execute("CREATE DATABASE IF NOT EXISTS Loja_RPG;")
        cursor.execute("USE Loja_RPG;")

        # --- Tabela: Cliente ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cliente (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            idade SMALLINT UNSIGNED,
            sexo ENUM('M', 'F', 'O'),
            data_nascimento DATE
        );
        """)

        # --- Tabela: Clientes Especiais ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes_especiais (
            cliente_id INT PRIMARY KEY,
            cashback DECIMAL(10,2) DEFAULT 0.00,
            FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
        """)

        # --- Tabela: Vendedor ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vendedor (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            causa_social VARCHAR(100),
            nota_media DECIMAL(3,1) DEFAULT 0.0
        );
        """)

        # --- Tabela: Produtos ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            quantidade_em_estoque INT UNSIGNED DEFAULT 0,
            valor DECIMAL(10,2) NOT NULL DEFAULT 0.00,
            observacoes TEXT,
            vendedor_id INT,
            FOREIGN KEY (vendedor_id) REFERENCES Vendedor(id)
                ON DELETE SET NULL
                ON UPDATE CASCADE
        );
        """)

        # --- Tabela: Transportadoras ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transportadoras (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cidade VARCHAR(100)
        );
        """)

        # --- Tabela: Venda ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Venda (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cliente_id INT,
            transportadora_id INT,
            data_hora DATETIME DEFAULT NOW(),
            endereco_des VARCHAR(100),
            valor_transp DECIMAL(10,2) DEFAULT 0.00,
            FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
                ON DELETE SET NULL
                ON UPDATE CASCADE,
            FOREIGN KEY (transportadora_id) REFERENCES transportadoras(id)
                ON DELETE SET NULL
                ON UPDATE CASCADE
        );
        """)

        # --- Tabela: Venda_Produtos ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS venda_produtos (
            venda_id INT,
            produto_id INT,
            quantidade INT UNSIGNED DEFAULT 1,
            PRIMARY KEY (venda_id, produto_id),
            FOREIGN KEY (venda_id) REFERENCES Venda(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
            FOREIGN KEY (produto_id) REFERENCES Produtos(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
        """)

        conn.commit()
        print("Todas as tabelas foram criadas (ou já existiam).")

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
        conn.rollback()

    finally:
        if cursor:
            cursor.close()
        desconectar(conn)


if __name__ == "__main__":
    criar_tabelas()
