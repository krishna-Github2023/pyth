# Dummy Python Code with Vulnerabilities and Duplications

def insecure_password_check(password):
    # Simulate insecure password check - never use this in real code
    if password == "admin123":
        print("Access granted")
    else:
        print("Access denied")

def sql_injection_vulnerability(user_input):
    # Simulate a SQL injection vulnerability - never use this in real code
    query = "SELECT * FROM users WHERE username='" + user_input + "';"
    print("Executing query:", query)

def duplicate_code_example():
    # Simulate duplicated code - avoid duplications in real code
    x = 10
    y = 5

    result1 = x + y
    print("Result 1:", result1)

    # Duplicated code
    result2 = x + y
    print("Result 2:", result2)

def main():
    # Simulate the main function
    password_input = input("Enter password: ")
    insecure_password_check(password_input)

    username_input = input("Enter username for SQL query: ")
    sql_injection_vulnerability(username_input)

    duplicate_code_example()

if __name__ == "__main__":
    main()
