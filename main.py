from database_connection import MySQLDatabase

if __name__ == '__main__':
    print("running")
    
    try:
        db = MySQLDatabase()
        print(f"starting..........\nStatus: {db.conn.is_connected()}")
    except ConnectionError as err:
        raise f"Erro ao conectar no banco....mensagem: {err}"