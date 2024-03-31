from datetime import datetime

import pytest

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
            self.connection = None

    def get_all(self):
        rows = list()
        query = """ SELECT id, income, expenditure, description, date_time, company_id 
                      FROM transaction;"""

        self.connect()
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        self.disconnect()

        return rows

    def insert_new(self, transaction_data):
        insert_transaction_template = """
        INSERT INTO transaction (income, expenditure, description, date_time, company_id) 
             VALUES (%(income)s, %(expenditure)s, "%(description)s", %(date_time)s, %(company_id)s)"""

        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(insert_transaction_template, transaction_data)
            self.connection.commit()

        self.disconnect()


# @pytest.mark.skip(reason='For debugging purpose')
def test_get_all():
    new_record = {
        'income': 0,
        'expenditure': 1,
        'description': 'test_get_all()',
        'date_time': datetime.now(),
        'company_id': 1,
    }

    transaction_obj = Transaction()
    before = transaction_obj.get_all()
    transaction_obj.insert_new(new_record)
    after = transaction_obj.get_all()

    print(f'BEFORE:\n"{before}"\nAFTER:\n{after}')
    assert len(before) + 1 == len(after)
