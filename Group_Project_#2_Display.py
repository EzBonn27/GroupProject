import sqlite3
def main():
    conn = sqlite3.connect('Student_Data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student_Info_Table")
    rows = cur.fetchall()

    print("Student Info Table:")
    print("===================")

    for row in rows:
        print(f"First Name: {row[0]}")
        print(f"Last Name: {row[1]}")
        print(f"Major: {row[2]}")
        print(f"GPA: {row[3]}")
        print(f"Age: {row[4]}")
        print(f"Address: {row[5]}")
        print(f"Phone Number: {row[6]}")
        print("")

    conn.close()
if __name__ == '__main__':
    main()