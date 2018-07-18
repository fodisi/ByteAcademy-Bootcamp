#!usr/bin/env python3
import sqlite3 as db


class Product():
    def get_product(self, name):
        with db.connect('products.db', check_same_thread=False) as conn:
            cur = conn.cursor()
            sql_cmd = """SELECT pk,name,price,picture 
                        FROM products WHERE name='{}';
                        """.format(name)
            cur.execute(sql_cmd)
            row = cur.fetchall()
            print(row)
            if len(row) > 0:
                return {
                    'id': row[0][0],
                    'name': row[0][1],
                    'price': row[0][2],
                    'picture': row[0][3]
                }
            else:
                return None
