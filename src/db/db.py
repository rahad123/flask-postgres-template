import psycopg2


def connect():
    # Define the connection parameters
    params = {
        'database': 'match360',
        'user': 'postgres',
        'password': '1234',
        'host': '192.168.0.131',
        'port': '5432'
    }

    try:
        # Attempt to establish a connection
        conn = psycopg2.connect(**params)
        print("Connected to PostgreSQL")
        return conn
    except psycopg2.Error as e:
        print("Error: Unable to connect to PostgreSQL")
        print(e)
        return None


# FETCHING DATA
def fetch(query):
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)

        data = cur.fetchall()

        print("Data retrieved from database")

        conn.commit()

        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
        return None
    finally:
        if conn is not None:
            conn.close()


#   EXECUTE QUERY


def fetch_data(query, *args):
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(query, args)

        data = cur.fetchall()

        print("Data retrieved from database")

        conn.commit()

        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
        return None
    finally:
        if conn is not None:
            conn.close()


#   INSERT DATA INTO TABLE
def insert_data(query, args):
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(query, args)

        conn.commit()

        print("Data inserted successfully")

        return True
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print("Error:", error)
        return error
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    pass
