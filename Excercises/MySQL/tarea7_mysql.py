import mysql.connector
import pandas as pd
import numpy as np

'''
Orden de ejecucion:
1. CREATE DATABASE
2. USE DATABASE o sino definirla en el connector como db = ""
3. CREATE TABLE nombre_tabla (Parametro TIPO_DATO TIPO_KEY, Parametro2 TIPO_DATO, Parametro3 TIPO_DATO ) #Recuerden que la PRIMARY KEY solo se define una por tabla
4. INSERT INTO nombre_tabla (Parametro, Parametro2, Parametro3) VALUES (%s, %s, %s) #Comenzar a actualizar los datos de la tabla
'''

try:
    db = mysql.connector.connect(
        host="localhost", #Host por default es localhost
        user="root", #Usuario definido en MySQL
        passwd="U$#gtr9W_)jfc:D3", #Aqui va la contraseña que definieron en MySQL
        db = "titanic" #Nombre de la base de datos solo hasta despues de haberla creado (Linea 24)
        )

    my_cursor = db.cursor()
    # my_cursor.execute("USE DATABASE titanic")
    # my_cursor.execute("DROP TABLE male_passengers")
    # my_cursor.execute("CREATE DATABASE titanic")
    # my_cursor.execute("CREATE TABLE male_passengers (PassengerId INT PRIMARY KEY, Name VARCHAR(255), Age FLOAT, Survived INT, Cabin VARCHAR(255))")
    # my_cursor.execute("CREATE TABLE female_passengers (PassengerId INT PRIMARY KEY, Name VARCHAR(255), Age FLOAT, Survived INT, Cabin VARCHAR(255))")
    # my_cursor.execute("ALTER TABLE male_passengers MODIFY Age float")

    #Abrir archivo csv con Pandas
    df = pd.read_csv('tarea7_mysql\\train.csv')

    #Define filter for Gender
    gender_male = df[df["Sex"] == "male"]
    gender_female = df[df["Sex"] == "female"]

    #Create sample of 100 random data from the filtered data
    data_females = gender_male[["PassengerId", "Name", "Age", "Survived","Cabin"]].replace(np.nan, '0', regex=True).sample(n=100)
    data_females = gender_female[["PassengerId", "Name", "Age", "Survived","Cabin"]].replace(np.nan, '0', regex=True).sample(n=100)

    #Create csv's with the filtered data for debugging purposes
    data_females.to_csv('tarea7_mysql\\male_db.csv', index=False)
    data_females.to_csv('tarea7_mysql\\female_db.csv', index=False)

    #Query for parameterized insert 
    query = "INSERT INTO male_passengers (PassengerId, Name, Age, Survived, Cabin) VALUES (%s, %s, %s, %s, %s)"

    #Iterating over 100 data
    for i in range(len(gender_male)):
        my_data = (data_females.iloc[i, 0].astype(str), data_females.iloc[i, 1], data_females.iloc[i, 2], data_females.iloc[i, 3].astype(str), data_females.iloc[i, 4])
        my_cursor.execute(query, my_data)
        db.commit()

except mysql.connector.Error as error:
    print("Error: {}".format(error))
finally:
    if db.is_connected():
        my_cursor.close()
        db.close()
        print("Conexion MySQL cerrada")