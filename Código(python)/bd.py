import mysql.connector

def conectar():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", #colocar a mesma senha do MySQL aqui.
        database="loja_rpg"
    )

    if conn.is_connected():
        print("Conexão bem sucedida!")
        return conn
    
    else:
        print("Falha na conexão.")
        return None
    
def desconectar(conn):
    if conn.is_connected():
        conn.close()
        print("Conexão encerrada.")
