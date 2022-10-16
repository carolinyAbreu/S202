from pprintpp import pprint as pp
from db.database import Graph


class PersonDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://34.201.33.19:7687',
                        user='neo4j', password='bend-humps-force')

    def create(self, teacher):
        return self.db.execute_query('CREATE (n:Teacher {name:$name, age:$age, area:$area}) return n',
                                     {'name': teacher['name'], 'age': teacher['age'], 'area': teacher['area']})
    
    def create(self, classes):
        return self.db.execute_query('CREATE (n:Classes {topic:$topic, time:$time}) RETURN n',
                                     {'topic': classes['topic'], 'time': teacher['time']})

    def create_relation(self, teacher, classes):
        return self.db.execute_query('MATCH (n:Person {name:$name1}), (m:Person {name:$name2}) CREATE (n)-[r:KNOWS{year: $year}]->(m) RETURN n, r, m',
                                     {'name1': person1['name'], 'name2': person2['name'], 'year': year})
    
    def create_relation(self, teacher, classes, year):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}), (m:Classes {topic:$topic}) CREATE (n)-[r:TEACH{year: $year}]->(m) RETURN n, r, m',
                                     {'name': teacher['name'], 'topic': classes['topic'], 'year': year})                                                                  