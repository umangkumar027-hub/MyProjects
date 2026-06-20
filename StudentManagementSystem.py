def addStudent(ID=None,name=None,classes=None,RollNo=None):
    data = {
        "ID" : ID,
        "Name" : name,
        "Class" : classes,
        "RollNo." : RollNo 
    }
    return data
    
def Viewer(data):
    print(list(data.items()))
    
def search(data):
    search_data = input("Enter value to search : ")
    found = False
    
    for key,value in data.items():
        if str(value) == search_data:
            print(f"Found -> {key} : {value}")
            found = True
            break
        
    if not found:
        print("I Couldn't find The search data...") 


def delete(data):
    delete = input("Enter Delete data : ")
    found = False
    
    for key,value in data.items():
        if str(value) == delete:
            del data[key]
            found = True
            break
        
    if not found:
        print("I couldn't find data..")


def savefile(data):
    with open("Students.txt","a") as f:
        f.write("{\n")
        for key,value in data.items():
           f.write(f"   {key} : {value}\n")   
           
        f.write("}\n\n")  
        
               
id = int(input("Enter ID : "))
name = (input("Enter Name : "))
classes = (input("Enter Class : "))
RollNo = int(input("Enter RollNo. : "))

data = addStudent(ID=id,name=name,classes=classes,RollNo=RollNo)
# search(data)
savefile(data)
