from database.connection import get_db_connection
from models.article import Article
from models.magazine import Magazine

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @classmethod
    def create_author(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO authors (name) VALUES (?)"
        cursor.execute(query, (name,))
        conn.commit()
        author_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return cls(author_id, name)

    def articles(self):
        """Fetch articles written by the author."""
        query = "SELECT id, title, content FROM articles WHERE author_id =?"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (self._id,))
            articles_data = cursor.fetchall()
        
        articles = [Article(*data) for data in articles_data]
        return articles

    def magazines(self):
        """Fetch magazines published by the author."""
        query = """
            SELECT magazines.id, magazines.name, magazines.category
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id =?
        """
        with self.conn.cursor() as cursor:
            cursor.execute(query, (self._id,))
            magazines_data = cursor.fetchall()
        
        magazines = [Magazine(*data) for data in magazines_data]
        return magazines

    def __repr__(self):
        return f'<Author {self._name}>'

