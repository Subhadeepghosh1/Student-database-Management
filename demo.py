import psycopg2

def create_data():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="rahul12345",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key,name text,address text,age int, number text);")
    print("student table created")
    conn.commit()
    conn.close()


def insert_data():
    name = input("Enter name")
    address = input("Enter address")
    age = int(input("Enter age"))
    number = input("Enter number")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="rahul12345",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("insert into students(name,address,age,number) values (%s,%s,%s,%s)",(name,address,age,number))
    print("Data added to students table")
    conn.commit()
    conn.close()


def delete_data():
    student_id = input('Enter the id of the student you want to delete')
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="rahul12345",host="localhost",port="5432")
    cur = conn.cursor()
    
    cur.execute("select * from students where student_id=%s",(student_id,))
    student = cur.fetchone()

    if student:
        print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
        choice = input("Are you sure you want to delete? (yes/no)")
        if choice.lower() == 'yes':
            cur.execute("delete from students where student_id=%s",(student_id,))
            print("student Record deleted")
        else:
            print("Cancelled")
    else:
        print("Student not found")

    conn.commit()
    conn.close()
            

def update_data():
    student_id = input("Enter id of student to be updated")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="rahul12345",host="localhost",port="5432")
    cur = conn.cursor()
    fields = {
        "1":("name","Enter the name"),
        "2":("address","Enter the address"),
        "3":("age","Enter the age"),
        "4":("number","Enter the number"),
    }
    print("Which field would you like to update")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    choice = input("Enter the number of the field you want to update")

    if choice in fields:
        field_name, prompt = fields[choice]
        new_val = input(prompt)
        sql = f"update students set {field_name}=%s where student_id=%s"
        cur.execute(sql,(new_val,student_id))
        print(f"{field_name} is updated successfully")
    else:
        print("Invalid Choice")


    print("Data Updated to students table")
    conn.commit()
    conn.close()

def read_data():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="rahul12345",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
    
    conn.close()


while True:
    print("\n welcome to the Database Management system")
    print("1.Crete table")
    print("2.Insert data")
    print("3.Read data")
    print("4.Update data")
    print("5.delete data")
    print("6.Exit")
    choice = input("Enter a choice (1-6): ")
    if choice =='1':
        create_data()
    elif choice =='2':
        insert_data()
    elif choice =='3':
        read_data()
    elif choice=='4':
        update_data()
    elif choice =='5':
        delete_data()
    elif choice=='6':
        break
    else:
        print("Invalid choice, Please enter a number between (1-6)")
