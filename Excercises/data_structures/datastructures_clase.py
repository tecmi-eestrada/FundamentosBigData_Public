def test(hola):
    if hola is True:
        print("Hola")

cualquier_cosa = "soy global"

#Funcion para convertir lista en diccionario
def convert_to_dict(registered_students):
    students_list = []
    for students in registered_students:
        student_dictionary = {}
        for pair_data in students:
            student_dictionary[pair_data[0]] = pair_data[1]
        students_list.append(student_dictionary)
    return students_list

#Funcion para validar si cumple con la mayoria de edad
def is_legal_age(students_list):
    for student in students_list:
        if student["age"] < 18:
            print(f"El estudiante {student['name']} es menor de edad")
        elif student["age"] == 18:
            print(f"El estudiante {student['name']} tiene 18 años")
        else:
            print(f"El estudiante {student['name']} es mayor de edad")

#Funcion para validar si el estudiante se encuentra registrado
def is_student_registered(name, student_list):
    for student in student_list:
        if name.lower() in student["name"]:
            print("El estudiante se encuentra registrado")
            break
        else:
            print("El estudiante no se encuentra registrado")

def print_something(to_be_printed):
    print(to_be_printed)

#Solicita al usuario la cantidad de estudiantes a registrar
# num_iterations = int(input("How many students would you like to register: "))

#Lista data_keys que almacena las llaves y lista data_lists que sera utilizada para almacenar las llaves y valores
data_keys = ["name", "age", "cellphone", "address"]
data_lists = []

#Iterador para recibir la informacion de los estudiantes a registrar
def get_data(num_iterations):
    while num_iterations > 0:
        data_values = []
        name = input("Student Name: ")
        data_values.append([data_keys[0], name.lower()])

        age = int(input("Student Age: "))
        data_values.append([data_keys[1], age])

        while True:
            cellphone = int(input("Student Cellphone: "))
            if len(str(cellphone)) == 10:
                break
            print("No es un numero valido, intente de nuevo")
        data_values.append([data_keys[2], cellphone])

        address = input("Student Address: ")
        data_values.append([data_keys[3], address.lower()])

        num_iterations -= 1
        data_lists.append(data_values)
        print("--------------------------")
    return data_lists

# students = convert_to_dict(data_lists)

# print(is_student_registered("luis", students))
# is_legal_age(students)
# print(convert_to_dict(data_lists))
# print(data_lists)
# test(True)