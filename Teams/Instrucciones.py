'''
Deberan crear un restaurante que tenga:
    -Nombre del negocio
    -Tipo de Comida (cocina oriental, cocina occidental, 
     comida rapida, comida regional, etc)
    -Año de fundacion
    -Nombre de la Mascota del restaurante

Para dicho restaurante, deberan crear la posibilidad de:
-Registrar platillos en el menu (deberan tener minimo 10 platillos)
    -Cada platillo debe contar con:
        -Nombre del platillo
        -Descripcion (ingredientes y cantidad)
        -Precio

-Registrar bebidas en el menu (deberan tener minimo 4 bebidas)
    -Cada bebida debe contar con:
        -Nombre de la bebida
        -Descripcion (ingredientes y cantidad)
        -Precio

-Registrar Extras en el menu (deberan tener minimo 8 extras)
    -Cada Extra debe contar con:
        -Nombre del extra
        -Descripcion (ingredientes y cantidad)
        -Precio

        -Deberan tener la posibilidad de vender por separado los platillos
-Deberan tener la posibilidad de convertirse a combo (platillo principal, bebida y extra):
    -El combo debe de ser una mezcla de cualquiera de los 3 anteriormente mencionados
    -Al costo del combo se le debera restar el 10% de la suma total de los platillos vendidos individualmente

-Debera desplegar en un menu TODOS los platillos, TODAS las bebidas y TODOS los extras
    -Para los combos pueden desplegar solo 3 que ustedes deseen
        -El combo debera tener su nombre
        -El combo debera tener su Descripcion
        -El combo debera tener su precio
    -Un cliente puede pedir un combo aunque no exista en el menu (estos combos no tendran nombre)

-Debera poder hacer una venta y registrarla en un ticket
    -Cada ticket de venta debera tener un ID, el cual estara constituido de 6 digitos aleatorios e irrepetibles
        -La venta sera la sumatoria de los elementos individualmente
        -La venta puede ser, en caso de combo, la sumatoria menos la deduccion del 10%
        -Todas las ventas deben calcular el IVA
'''
