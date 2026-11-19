import sqlite3
import os
DATABASE_PATH=os.path.join(
    os.path.dirname(__file__),
    "clouddesk.db"
)

def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory=sqlite3.Row
    return connection

def initialize_database():
    connection=get_db_connection()
    connection.execute("""
                       
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            
        """)
    connection.commit()
    connection.close()
    
    
