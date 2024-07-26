# step 1: creating a file
# file = open("student.txt","x")

# step 2: writing into the file
file = open("student.txt","w")
print(file.write("list of students in senior five"))
file.close()
# step 3: reading a file
file = open("student.txt","r")
print(file.read())
file.close
# step 4: append a file
file = open("student.txt","a")
print(file.write("nsereko brian,nambi joy, nankya jemimah"))
file.close()
#  exceptional handling
try:
    file = open("student.txt","x")
    file = open("student.txt","a")
    print(file.write("that is senior five"))
    file.close()
except Exception:
    print("file aready exists")
finally:
    print("task completed")
import os
def remove():
    os.remove("example.txt")
    print("file deleted successfully")
remove()
    
            
