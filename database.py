import psycopg2


DATABASE = "jiali_huang"
USER = "jiali_huang"
PASSWORD = "hjkgs7g8s678gg"
HOST = "imperial-2025.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com"
PORT = "5432"

def get_db_connection():
    """
    Establishes and returns a connection to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            dbname=DATABASE,
            port=PORT
        )
        print("Connected to the database successfully!")
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

# Get the database connection
conn = get_db_connection()


cur = conn.cursor()

# Create users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL
);
""")

# Create sticky_notes table
cur.execute("""
CREATE TABLE IF NOT EXISTS sticky_notes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    note TEXT NOT NULL
);
""")

# Create tasks table
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    task TEXT NOT NULL
);
""")

# Create quotes table
cur.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id SERIAL PRIMARY KEY,
    quote TEXT NOT NULL,
    emoji TEXT
);
""")

# Insert predefined motivational quotes if the table is empty
cur.execute("SELECT COUNT(*) FROM quotes;")
count = cur.fetchone()[0]

if count == 0:
    cur.execute("""
    INSERT INTO quotes (quote, emoji) VALUES
    ('Believe in yourself!', '💪'),
    ('Keep pushing forward.', '🚀'),
    ('Success is no accident.', '🎯'),
    ('Stay positive and work hard.', '😊');
    """)

conn.commit()
cur.close()
conn.close()
