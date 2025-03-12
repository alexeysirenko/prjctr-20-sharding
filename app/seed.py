#!/usr/bin/env python3

import os
import psycopg2
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def create_books_table():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS books")
        cur.execute("""
            CREATE TABLE books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                isbn VARCHAR(20) UNIQUE NOT NULL,
                year INTEGER CHECK (year > 0),
                genre VARCHAR(100),
                publisher VARCHAR(255),
                pages INTEGER CHECK (pages > 0),
                language VARCHAR(50),
                description TEXT,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cur.execute("CREATE INDEX idx_books_isbn ON books (isbn)")
        
        conn.commit()
        logger.info("Books table created successfully!")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    logger.info("Starting database setup...")
    create_books_table()
    logger.info("Database setup completed!")