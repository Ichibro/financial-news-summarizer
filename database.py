import sqlite3

def initialize_database():
    conn = sqlite3.connect('financial_news.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            url TEXT,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_articles(articles):
    conn = sqlite3.connect('financial_news.db')
    cursor = conn.cursor()

    # Insert articles
    for article in articles:
        cursor.execute('''
            INSERT INTO articles (title, description, url, date)
            VALUES (?, ?, ?, ?)
        ''', (article["title"], article["description"], article["url"], article["date"]))

    conn.commit()
    conn.close()
