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
        return f'{self.id}. {self.name}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise TypeError("name must be a non-empty string")
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise TypeError("website must be a non-empty string!")

    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Brand instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS brands(
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
            DROP IF EXISTS TABLE brands;
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
            UPDATE brands
            SET name = ?, description = ?
            WHERE id = ?
            """
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
    
    @classmethod
    def get_all(cls):
        """returns list of all brands"""
        sql = """
            SELECT * FROM brands
        """
        rows = CURSOR.execute(sql,).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    # useless in our case
    @classmethod
    def find_by_id(cls, id):
        """return a brand object corresponding to the tabke row matching the speciifed primary key / id"""
        sql = """
            SELECT * FROM brands
            WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone() 
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """return a brand object corresbonding to the table row matching the specified name"""
        sql = """
            SELECT * FROM brands
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def products(self):
        """return list of products associated with current brand"""
        from models.product import Product
        sql = """
            SELECT * FROM products
            WHERE brand_id is ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        # breakpoint()
        return [ Product.instance_from_db(row) for row in rows]
    
    
    # def property_function(attribute,type):
    #     @property
    #     def attribute(self):
    #         return getattr(self, f'_{attribute}')
        
    #     @attribute.setter
    #     def attribute(self, attribute):
    #         if isinstance(attribute, type) and len(attribute):
    #             setattr(self,f'_{attribute}', attribute)
    #         else:
    #             raise TypeError(f'name must be a non-empty {type}')
            
    #     return attribute, attribute.setter
    
    # property_function("name",str)
    # property_function("description",str)