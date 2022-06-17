from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls, data):
        query = "SELECT * "
        query += "FROM dojos JOIN ninjas ON dojos.id=ninjas.dojo_id "
        query += "WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) "
        query += "VALUES(%(fname)s, %(lname)s, %(age)s, %(dojo_name)s);"
        print(query)
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results