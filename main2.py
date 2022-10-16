from EscolaDB import Person
from pprintpp import pprint as pp

dao = Person()

 #CRIANDO 4 PROFESSORES

teacher = {
    'name': 'Renzo',
    'age': 31,
    'area': 'Computação' 
}
dao.createTeacher(teacher)

teacher = {
    'name': 'Marcelo',
    'age': 32,
    'area': 'Software' 
}
dao.createTeacher(teacher)

teacher = {
    'name': 'Baratella',
    'age': 49,
    'area': 'Automação' 
}
dao.createTeacher(teacher)

teacher = {
    'name': 'Justino',
    'age': 84,
    'area': 'Telecomunicações' 
}
dao.createTeacher(teacher)

#CRIANDO 2 AULAS

classes = {
    'topic': 'Banco de Dados',
    'time': '1h 40min'
}
dao.createClass(classes)

classes = {
    'topic': 'Paradigmas de Programação',
    'time': '1h 40min'
}
dao.createClass(classes)

#CRIANDO RELACIONAMENTO

year = 2013

dao.create_relation(teacher, classes, year)
