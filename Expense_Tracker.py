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
            
            

amount = int(input("Enter The Amount : "))
category = (input("Enter The Category : "))
date = (input("Enter The Date : "))
description = (input("Enter The Description : "))

expense = Expense(Amount=amount,Category=category,Date=date,Description=description)
# Viewer(expense)
mulit_info(expense)

view_all()


