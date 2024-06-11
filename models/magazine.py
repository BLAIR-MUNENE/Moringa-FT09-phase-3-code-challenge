from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("Cannot set id after instantiation")

    @property
    def name(self):
        self.cursor.execute("SELECT name FROM magazines WHERE id=?", (self._id,))
        result = self.cursor.fetchone()
        return result[0] if result else ""

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self.cursor.execute("UPDATE magazines SET name=? WHERE id=?", (value, self._id))
            self.conn.commit()
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        self.cursor.execute("SELECT category FROM magazines WHERE id=?", (self._id,))
        result = self.cursor.fetchone()
        return result[0] if result else ""

    @property
    def category(self):
        return self._category


    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")
    
    @staticmethod
    def save_to_database(self):
        self.cursor.execute("INSERT magazines (id, name, category) VALUES (?,?,?)", (self._id, self._name, self._category))
        self.conn.commit()


