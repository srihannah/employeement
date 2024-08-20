import mysql.connector


class EmployeeManagement:
    def __init__(self):
        # Connect to MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hannah@45",
            database="employee_db"
        )
        self.cursor = self.conn.cursor()

    def add_employee(self):
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))
        department = input("Enter employee department: ")
        email = input("Enter employee email: ")
        phone = input("Enter employee phone: ")
        hire_date = input("Enter employee hire date (YYYY-MM-DD): ")

        query = """
        INSERT INTO employees (name, position, salary, department, email, phone, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (name, position, salary, department, email, phone, hire_date))
        self.conn.commit()
        print("Employee added successfully.")

    def view_employees(self):
        query = "SELECT * FROM employees"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print("Employee Records:")
        for row in results:
            print(
                f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}, Department: {row[4]}, Email: {row[5]}, Phone: {row[6]}, Hire Date: {row[7]}")

    def update_employee(self):
        emp_id = int(input("Enter the ID of the employee to update: "))
        name = input("Enter new employee name: ")
        position = input("Enter new employee position: ")
        salary = float(input("Enter new employee salary: "))
        department = input("Enter new employee department: ")
        email = input("Enter new employee email: ")
        phone = input("Enter new employee phone: ")
        hire_date = input("Enter new employee hire date (YYYY-MM-DD): ")

        query = """
        UPDATE employees
        SET name = %s, position = %s, salary = %s, department = %s, email = %s, phone = %s, hire_date = %s
        WHERE id = %s
        """
        self.cursor.execute(query, (name, position, salary, department, email, phone, hire_date, emp_id))
        self.conn.commit()
        print("Employee updated successfully.")

    def delete_employee(self):
        emp_id = int(input("Enter the ID of the employee to delete: "))
        query = "DELETE FROM employees WHERE id = %s"
        self.cursor.execute(query, (emp_id,))
        self.conn.commit()
        print("Employee deleted successfully.")

    def search_employee(self):
        search_term = input("Enter a name or email to search for: ")
        query = """
        SELECT * FROM employees
        WHERE name LIKE %s OR email LIKE %s
        """
        self.cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
        results = self.cursor.fetchall()
        if results:
            print("Search Results:")
            for row in results:
                print(
                    f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}, Department: {row[4]}, Email: {row[5]}, Phone: {row[6]}, Hire Date: {row[7]}")
        else:
            print("No matching employees found.")

    def run(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add employee")
            print("2. View employees")
            print("3. Update employee")
            print("4. Delete employee")
            print("5. Search employee")
            print("6. Exit")

            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.delete_employee()
            elif choice == '5':
                self.search_employee()
            elif choice == '6':
                print("Exiting the system. Have a great day!")
                self.cursor.close()
                self.conn.close()
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    employee_system = EmployeeManagement()
    employee_system.run()
