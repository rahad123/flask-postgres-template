import psycopg2


class UserService:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def create_user(self, username, email):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT insert_user(%s, %s);", (username, email))
            user_id = cursor.fetchone()[0]
        self.conn.commit()
        return user_id

    def get_user(self, user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
            user = cursor.fetchone()
        return user

    def update_user(self, user_id, new_username, new_email):
        with self.conn.cursor() as cursor:
            cursor.execute("UPDATE users SET username = %s, email = %s WHERE id = %s;",
                           (new_username, new_email, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
