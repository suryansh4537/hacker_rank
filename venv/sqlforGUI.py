import mysql.connector

mydb = mysql.connector.connect(
    user="root", passwd="", host="127.0.0.1", database="banana"
)
mycursor = mydb.cursor()
class DBase:

    def addCustomer(self,abc):
        add="insert into testing values(null,'{}','{}','{}','{}')".format(abc.name,abc.age,abc.hobby,abc.aim)


        mycursor.execute(add)
        mydb.commit()

    def updatCustomer(self,abc):
        update="update testing set name='{}',age='{}',hobby='{}',aim='{}' where id={}".format(abc.name,abc.age,abc.hobby,abc.aim,abc.id)
        mycursor.execute(update)
        mydb.commit()

    def deleteCustomer(self,abc):
        delete="delete from testing where id={}".format(abc)
        mycursor.execute(delete)
        mydb.commit()

    def showcustomer(self,abc):
        show="select * from testing where id={}".format(abc.id)
        mycursor.execute(show)
        row=mycursor.fetchall()
        for i in row:
            print(i)

    def showall(self):
        show="select * from testing"

        mycursor.execute(show)
        result=mycursor.fetchall()
        return result


class Customer:
    def __init__(self,name,age,hobby,aim):
        self.name=name
        self.age=age
        self.hobby=hobby
        self.aim=aim
'''
print("OPTIONS")
print("1.ADD customer\n2.Update customer\n3.Delete customer\n4.Customer Details")
myobject = Customer(None, None, None, None)
myobject1 = myobject
databaseobject = DBase()
choice=int(input("Enter your choice="))
if choice==1:

        myobject1.name=input("Enter name=")
        myobject1.age=input("Enter age=")
        myobject1.hobby=input("Enter hobby=")
        myobject1.aim=input("What is your aim=")

        databaseobject.addCustomer(myobject1)
        print("Customer Added")

elif choice==2:

        myobject1.id=input("Enter the id of the customer=")
        databaseobject.showcustomer(myobject1)
        myobject1.name = input("Enter name=")
        myobject1.age = input("Enter age=")
        myobject1.hobby = input("Enter hobby=")
        myobject1.aim = input("What is your aim=")
        databaseobject.updatCustomer(myobject1)
        print("updated")

elif choice==3:

        myobject1.id=input("enter id=")
        databaseobject.deleteCustomer(myobject1)
        print("deleted!!")

else:

    databaseobject.showall()'''
