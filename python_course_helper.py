import sqlite3 as lite


# functionality goes here

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(Id INT PRIMARY KEY AUTOINCREMENT,name TEXT, description TEXT,price TEXT,is_private BOOLEAN NOT NULL DEFAULT )")
        except Exception:
            print("Unable to create a DB !")
    # TODO: create data

    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                )
                return True
        except Exception:
            return False
    # TODO: fetch  data

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False
    # TODO: delete data

    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor
                sql= "DELETE  FROM courses WHERE id=?"
                cur.execute(sql,[id])
                return True
            
        except Exception:
            return False


# TODO:provide interface to user
def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")
    
    db = DatabaseManage()
    
    print("#"*40)
    print("\n :: User Manual\n")
    print("#"*40)
    
    print('1. Insert a new Course\n')
    print('2. Show all courses\n')
    print('3. Delete a course(NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")
    
    choice = input("\n Enter a choice: ")
    
    if choice == "1":
        name=input("\n Enter course name:")
        description=input("\n Enter course description:")
        price=input("\n Enter course price:")
        private=input("\n Is this course private(0/1):")
        
        if db.insert_data([name,description,price,private]):
           print("Course was inserted successfully")
        else:
            print("OOPS Something went wrong")
    elif choice == "2":
        print("\n::Course List ::")
        for index,course in enumerate(db.fetch_data()):
           print("\n Serial Number:" + str(index+1))
           print("\n Course ID:" + str(course[0]))
           print("\n Course Name:" + str(course[1]))
           print("\n Course description:" + str(course[2]))
           print("\n Course Price:" + str(course[3]))
           private= 'Yes' if course[4] else 'NO'
           print("Is Private :" + private)
           print ("\n")
        
    elif choice == "3":
        record_id=input("Enter the course ID: ")
        if db.delete_data(record_id):
            print("Course was deleted successfully")
        else:
            print("OOPS,something went wrong")
    else:
        print("\n BAD CHOICE")
        
        
if __name__=="__main__":
    main()