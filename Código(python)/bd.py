import mysql.connector

def conectar():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", #colocar a mesma senha do MySQL aqui.
        database="Loja_RPG"
    )
    return conn

def desconectar(conn):
    if conn and conn.is_connected():
        conn.close()
