from database.connection import get_db_connection
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id
   
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    @classmethod
    def create_article(cls, author, magazine, title, content):
       
        conn = get_db_connection()
        query = """
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?,?,?,?)
        """
        with conn.cursor() as cursor:
            cursor.execute(query, (title, content, author.id, magazine.id))
            conn.commit()
            article_id = cursor.lastrowid
        return cls(article_id, title, content, author.id, magazine.id)

    def __repr__(self):
        return f'<Article {self.title}>'
