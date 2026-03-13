
#ASSIGNMENT SET 1 — Multi-Level Verification System

security_code = int(input("Enter the security code: "))

if security_code == 5566:
    department = input("Department name: ")

    if department == "Finance":
        print("Move to Condition 3:", department)

        access_level = int(input("Enter your access level: "))

        if access_level >= 5:
            print("Access Granted: Welcome to the meeting room.")
        else:
            print("Insufficient access level.")

    else:
        print("Access denied: Department not allowed")

else:
    print("Invalid security code.")

#ASSIGNMENT SET 2 — Online Exam Login    

registration_number = int(input("Enter your registration number: "))

if registration_number == 1221:
    print("Go ahead")

    subject = input("Enter the subject name: ")

    if subject == "Python":
        print("Continue to next step")

        password = int(input("Enter the password: "))

        if password == 8888:
            print("Login successful")
        else:
            print("Incorrect password")

    else:
        print("Subject not selected")

else:
    print("Registration failed")
  
