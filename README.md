# MR Rose - Inventory App

MR Rose is an basic inventory app to help you track your products.

## Installation

1. install dependencies and enter your virtual environment.

```bash
pipenv install
pipenv shell
```
2. run python lib/cli.py to enter app

```bash
python lib/cli.py
``` 
  
## Usage
- follow instructions prompted. from main page you can view a product summary or access the brands that you have in store. 
```
********************************************
*    Welcome to MR Rose - Inventory App    *
********************************************
     Please choose from the following:       

     Type b to see the Brands in store  
     Type p to see the Products summary 
     Type e to Exit                     
--------------------------------------------
> 
```
- from brands page you can add, view, update or delete a brand
```
      *******************        
------    Brands Page    -------

1. sabi
2. L'occitane
3. Le labo
4. aesop
5. byredo

--------------------------------
Please choose from the following:

     Type a to Add a brand
     Type v to View a brand details
     Type u to Update a brand
     Type d to Delete a brand
     Type m for Main Menu
     Type e to Exit
> 
```
- inside a brand you can add, view, update or delete a product
```
---------   sabi  -----------

1. furah
2. fleur noire
3. naked

---------------**---------------
Please choose from the following:

     Type a to Add a product
     Type v to View a product details
     Type u to Update a product
     Type d to Delete a product
     Type b for Brands
     Type e to Exit
> 
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MRRose](https://www.essentialsabi.com)