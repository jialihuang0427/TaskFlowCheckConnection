import psycopg2

DATABASE = "jiali_huang"
USER = "jiali_huang"
PASSWORD = "hjkgs7g8s678gg"
HOST = "imperial-2025.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com"
PORT = "5432"


def reset_users():
    conn = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        dbname=DATABASE,
        port=PORT
    )
    cur = conn.cursor()
    
    # Truncate users table safely
    cur.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
    conn.commit()

    cur.close()
    conn.close()
    print("All users deleted.")