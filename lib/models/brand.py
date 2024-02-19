# lib/models/brand.py
from models.__init__ import CURSOR, CONN

class Brand:

    # Dictionnary of brand objects saved to the database.
    all = {}

    def __init__(self, name, description, id= None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f"Brand: {self.name}, specializes in {self.description}"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Brand instances"""
        sql = """
            CREATE TABLE IF NOT EXIST brands(
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
            )
        """
        CURSOR.execute(sql,)
        CONN.commit()

    # this hsouldn't be necessary for the client. only for developper
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Brand instances """
        sql = """
            DROP IF EXIST TABLE brands;
        """
        CURSOR.execute(sql,)
        CONN.commit()

    def save(self):
        """saves a Brand instance"""
        sql = """
            INSERT INTO brands(name, description)
            VALUES(?,?)
        """
        CURSOR.execute(sql,(self.name, self.description,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id]= self

    @classmethod
    def create(cls, name, description):
        brand = cls(name, description)
        brand.save()
        return brand
    
    def update(self):
        """update a brand instance. name or description"""
        sql = """
            UPDATE brands(
            SET name = ?, description = ?
            WHERE id = ?
            )"""
        CURSOR.execute(sql, (self.name, self.description, self.id))
        CONN.commit()

    def delete(self):
        "delete a brand instance"
        sql = """
            DELETE FROM brands
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        # delete the dictionary entry using the id as the key
        del type(self).all[self.id]
        # set the id to None

    @classmethod
    def instance_from_db(cls,row):
        """obtain a row/instance from the brands table"""
        # check the brands dictionary from instance using the row's primary key
        brand = cls.all.get(row[0])
        if brand:
            #ensure attributes match row values in case local instance was modified.
            brand.name = row[1]
            brand.description = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            brand = cls(row[1], row[2])
            brand.id = row[0]
            cls.all[brand.id] = brand
        return brand