from re import I
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Universe2003",
  database="python"
)

cursor = mydb.cursor()


def search_chemical(cas_number):
    sql = f'SELECT name FROM chemical WHERE cas_number = {cas_number}'
    cursor.execute(sql)
    myresult = cursor.fetchall()
    return myresult[0][0]




class Chemical:
    def __init__(self,name,cas_number):
         try:
            self.name = name
            self.cas_number = cas_number
            print(f'Chemical with Name: {self.name} and CAS Number: {self.cas_number} created')
         except TypeError:
            print("Name and CAS number not specified")    
    
              

    def show(self):
        print(f'Chemical Name : {self.name} and CAS Number: {self.cas_number}')

    def save(self):
        sql = "INSERT INTO chemical (name, cas_number) VALUES (%s, %s)"
        val = (self.name, self.cas_number)
        cursor.execute(sql, val)
        mydb.commit()
        print(f'Chemical name: {self.name} and CAS Number: {self.cas_number} saved in Database.')
        



print(search_chemical("2584"))



    




