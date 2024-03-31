from .my_sql_connection import connect_to_mysql

CONFIG = {
    'host': '127.0.0.1',
    'port': 1521,
    'user': 'root',
    'password': '',
    'database': 'learn_dj',
}


# Create your models here.
class Transaction:
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = connect_to_mysql(CONFIG, attempts=3)

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_all(self):
        rows = list()
        self.connect()
        query = """ SELECT id, income, expenditure, description, date_time, company_id 
                      FROM transaction;"""

        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        self.disconnect()

        return rows

def test_this():
    all_transactions = {'transactions': Transaction().get_all()}
    print('Ho!')
