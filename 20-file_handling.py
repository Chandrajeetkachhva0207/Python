import os

filename = "demo.txt"

# 1. Create & Write File
with open(filename, "w") as file:
    file.write("Hello, this is a demo file.\n")
    file.write("This line is written using Python.\n")

print("File created and data written.\n")

# 2. Read File
print("Reading file content:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

# 3. Append Data
with open(filename, "a") as file:
    file.write("This line is appended later.\n")

print("\nData appended successfully.\n")

# 4. Read File Line by Line
print("Reading file line by line:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

# 5. Check if File Exists
print("\nChecking if file exists:")
if os.path.exists(filename):
    print("File exists.")
else:
    print("File does not exist.")

# 6. Delete File
delete = input("\nDo you want to delete the file? (yes/no): ")

if delete.lower() == "yes":
    os.remove(filename)
    print("File deleted.")
else:
    print("File not deleted.")