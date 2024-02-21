# lib/models/product.py 
from models.__init__ import CONN, CURSOR
from models.brand import Brand

class Product:

    all={}

    def __init__(self, name, description, quantity, price, brand_id, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.brand_id = brand_id

    def __repr__(self) -> str:
        return (f'{self.id}. {self.name} | quantity: {self.quantity}')
    
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
            raise TypeError("description must be a non-empty string")
        
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
        else:
            raise TypeError("quantity must be an integer")
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self._price = price
        else:
            raise TypeError("price must be a non-empty string")
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and len(brand):
            self._brand = brand
        else:
            raise TypeError("brand must be a non-empty string")
        
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

    # name, name.setter = property_function(name)
    # description, description.setter = property_function(description)
    # quantity, quantity.setter = property_function(quantity)
    # price, price.setter = property_function(price)

    @classmethod
    def create_table(cls):
        """create a products table to persist the attributes of Product instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            quantity INTEGER,
            price INTEGER,
            brand_id INTEGER,
            FOREIGN KEY (brand_id) REFERENCES brands (id)) 
        """
        CURSOR.execute(sql,)
        CONN.commit()

    def save(self):
        """save the attribute of a product instance"""
        sql = """
            INSERT INTO products(name, description, quantity, price, brand_id)
            VALUES(?,?,?,?,?)
        """
        CURSOR.execute(sql,(self.name, self.description, self.quantity, self.price, self.brand_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        """delete the attributes of a product instance"""
        sql = """
            DELETE FROM products
            WHERE id is ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        # breakpoint()
        del type(self).all[self.id]
        self.id = None
        # breakpoint()

    def update(self):
        """Update the table row corresponding to the current product instance"""
        sql = """
            UPDATE products
            SET name = ?, description = ?, quantity = ?, price = ?, brand_id = ?
            WHERE id = ?
            """
        CURSOR.execute(sql,(self.name, self.description, self.quantity, self.price, self.brand_id, self.id))
        CONN.commit()
        

    @classmethod
    def find_by_id(cls, _id):
        sql = """
            SELECT * FROM products
            WHERE brand_id is ?
        """

        row = CURSOR.execute(sql, (_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
        

    @classmethod
    def find_by_name(cls, name):
        """return instance based on name"""
        sql ="""
            SELECT * FROM products
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        CONN.commit()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def create(cls, name, description, quantity, price, brand_id):
        """Initialize a product instance and saves it to the products table"""
        product = cls(name,description,quantity, price, brand_id)
        product.save()
        return product
    
    @classmethod
    def instance_from_db(cls, row):
        """returns a product object having the attribute values from the table row."""
        product = cls.all.get(row[0])
        if product:
            product.name = row[1]
            product.description = row[2]
            product.quantity = row[3]
            product.price = row[4]
            product.brand_id = row[5]
        else:
            product = cls(row[1], row[2], row[3], row[4],row[5])
            product.id = row[0]
            cls.all[product.id]= product
        return product
    
    @classmethod
    def get_all(cls):
        """retrieves all the product instances"""
        sql = """
            SELECT * FROM products
            """
        rows = CURSOR.execute(sql).fetchall()
        CONN.commit()
        return [Product.instance_from_db(row) for row in rows]
     
