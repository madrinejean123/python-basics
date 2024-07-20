import os
# steps of working with files in python
# step 1.create and open a file
# file = open("newfile.txt","x")

# # step 2. reading a file
# file = open("newfile.txt","r")
# print(file.read())
# file.close()

# # step 3. writing in a file
# file = open("newfile.txt","w")
# print(file.write("today is a saturday"))
# file.close()

# # step 4.appending a file
# file = open("newfile.txt","a")
# print(file.write("and am going to school"))
# file.close()

try:
    file = open("newfile.txt","x")
    file = open("newfile.txt","w")
    print(file.write("my name is"))
    file.close()
except Exception:
    print("file arleady exists")
finally:
    print("completed")
import os
def remove():
    os.remove("newfile.txt")
    print("file has been deleted successfully")
remove()


print("hello world")