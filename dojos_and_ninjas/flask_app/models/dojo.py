from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * from dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos(name) "
        query += "VALUES(%(dojo_name)s);"
        print(query)
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "from dojos "
        query += "WHERE id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(results[0])