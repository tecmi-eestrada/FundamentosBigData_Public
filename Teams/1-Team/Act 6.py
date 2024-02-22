class Restaurante: #Sushi Street
    platillos=[" Sushi California-------------------------------------------------------------$70 Surimi,queso crema, pepino, aguacate,por fuera ajonjoli"]
    año_de_fundacion=1998

    def __init__(self, nombre, tipo_restaurante,fundacion,nombre_mascota):

        self.identidad= nombre 
        self.tipo= tipo_restaurante
        self.fundacion= fundacion 

    def __str__(self): 
        return f"Bienvenidos a {self.identidad}-{self.tipo},fundado en el año {self.año_de_fundacion} "
   
    def entrega_de_menu(self):
        menu= f"""
            Bienvenidos a {self.identidad}
                Menu
                {self.platillos[0]}
                Comidas 
                Sushi California-------------------------------------------------------------$70
                    Surimi,queso crema, pepino, aguacate,por fuera ajonjoli
                Sushi Philadelphia-----------------------------------------------------------$70
                    Surimi,tampico,agauacte, pepino, por fuera queso crema y ajonjoli 
                Sushi Camaron Roll-----------------------------------------------------------$85
                    Camaron, aguacate, queso crema, pepino, y por fuera tampico 
                Sushi River Roll-------------------------------------------------------------$95
                    Camaron, surimi, queso crema, aguacate y furikake de camaron 
                Sushi Geisha-----------------------------------------------------------------$110
                    Camaron empanizado, tampico, cebollin, queso crema, cebolla crujiente
                Salmon Grill-----------------------------------------------------------------$110
                    Salmon, camaron, queso crema, aguacate, por fuera aderrezo tatrtara
                Street Roll------------------------------------------------------------------$105
                    Arroz frito, camaron, aguacate, por fuera chipotle y salsa anguila
                Arroz frito -----------------------------------------------------------------$65
                    Arroz acompañado con verduras y aderezo al gusto 
                Arroz con camaron------------------------------------------------------------$80
                    Arroz mixto acompañado con camaron
                Arroz con carne--------------------------------------------------------------$75
                    Arroz mixto acompañado con carne 
                
                Bebidas 
                Refresco 500ml---------------------------------------------------------------$25
                    Sabor Cola 
                Refresco 500ml---------------------------------------------------------------$25
                    Sabor Toronja
                Refresco 500ml---------------------------------------------------------------$25
                    Sabor Manzana 
                Refresco 500ml---------------------------------------------------------------$25
                    Sabor Ponche
                Agua natural 1lt-------------------------------------------------------------$45
                    Sabor Jamaica 
                Agua natural 1lt-------------------------------------------------------------$45
                    Sabor Horchata

                Extras 
                Aderezo 50 ml---------------------------------------------------------------$18
                    Aderezo sabor chipotle 
                Aderezo 50 ml---------------------------------------------------------------$18
                    Aderezo ranch
                Aderezo 50 ml---------------------------------------------------------------$18
                    Aderezo blue chesse
                Salsas 50 ml----------------------------------------------------------------$18
                    teriyaki
                Salsas 50 ml----------------------------------------------------------------$18
                    Soya 
                Pasta tampico 250 gr--------------------------------------------------------$25
                    Surimi, verdudras, aderezo ranch 
                Ensalada 250 gr-------------------------------------------------------------$25
                    Pepino, zanahoria, betabel, ajonjoli
                Vinagreta  50ml-------------------------------------------------------------$25
                    Vinagre, aceites vegetales
        """
        return menu 
       





miRestaurante= Restaurante("Sushi Street","Comida Oriental",1998,"Sushikito")
print(miRestaurante.entrega_de_menu())
    
