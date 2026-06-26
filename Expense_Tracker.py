data = []
def Expense(Amount=None,Category=None,Date=None,Description=None):
    expense = {
        "Amount" : Amount,
        "Category" : Category,
        "Date" : Date,
        "Description" : Description
    }

    return expense


def Viewer(expense):
    for keys,values in expense.items():
        print(f"{keys} : {values}\n")
        

def mulit_info(expense):
    data.append(expense)
    return data
    
def view_all():
    for i in data:
        print("-" * 20)
        for key,value in i.items():
            print(f"{key} : {value}")
            
def savefile():
    with open("Expense.txt","a") as f:
        
        f.write("Expenses:\n")
        f.write("-" * 20 + "\n")
        for expense in data:
            f.write("{\n")
            for key,value in expense.items():
                f.write(f"   {key} : {value}\n")    
            f.write("}\n\n")  

        summary = {}
        for i in data:
            Category = i["Category"]
            amount = i["Amount"]
        
            summary[Category] = summary.get(Category,0) + amount
        
        f.write("\nCategory Wise Expenses\n")
        f.write("-" * 25 + "\n")
    
        for category,total in summary.items():
            f.write(f"{category} : ₹{total}\n")
        
        
        
while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Save Expenses")
    print("5. Exit")

    choice = input("Enter Choice: ")

    match choice:

        case "1":
            view_all()


        case "2":
            savefile()

        case "3":
            print("Thank You For Using Expense Tracker")
            break

        case _:
            print("Invalid Choice")



