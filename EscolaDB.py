from pprintpp import pprint as pp
from db.database import Graph


class Person(object):
    def __init__(self):
        self.db = Graph(uri='bolt://34.201.33.19:7687',
                        user='neo4j', password='bend-humps-force')

    def createTeacher(self, teacher):
        return self.db.execute_query('CREATE (n:Teacher {name:$name, age:$age, area:$area}) return n',
                                     {'name': teacher['name'], 'age': teacher['age'], 'area': teacher['area']})
    
    def createClass(self, classes):
        return self.db.execute_query('CREATE (n:Classes {topic:$topic, time:$time}) RETURN n',
                                     {'topic': classes['topic'], 'time': classes['time']})
    
    def create_relation(self, teacher, classes, year):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}), (m:Classes {topic:$topic}) CREATE (n)-[r:TEACH{year: $year}]->(m) RETURN n, r, m',
                                     {'name': teacher['name'], 'topic': classes['topic'], 'year': year})   