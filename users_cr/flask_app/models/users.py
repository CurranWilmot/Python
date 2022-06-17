from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE id=%(u_id)s;"
        print(query)
        results = connectToMySQL('users').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * from users;"
        results = connectToMySQL('users').query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) "
        query += "VALUES(%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL('users').query_db(query, data)
        return results

    @classmethod
    def update_user(cls, data):
        query = "DELETE FROM users "
        query += "WHERE id = %(u_id)s"
        query += "SET "
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def remove_user(cls, data):
        query = "DELETE FROM users "
        query += "WHERE id = %(u_id)s;"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users "
        query += "SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s "
        query += "WHERE id = %(u_id)s;"
        return connectToMySQL('users').query_db(query, data)