from database import sesija, Employee, Product, Sale

"""user1 = User(name="Nenad", age=22, email="email@gmail.com")
sesija.add(user1)
sesija.commit()"""

"""
emp1 = Employee(full_name="John Doe",
                email="mail@example.com",
                age=40,
                position="Sales",
                salary=40000,
                years_in_company=5)
sesija.add(emp1)
sesija.commit()
print("Vraboteniot e zapisan")
"""

def insert_employee(sesija, full_name, email, age, position, salary, years_in_company):
    emp1 = Employee(full_name=full_name,
                    email=email,
                    age=age,
                    position=position,
                    salary=salary,
                    years_in_company=years_in_company)    
    sesija.add(emp1)
    sesija.commit()
    print(f"Vraboteniot {full_name} e vnesen")
    return emp1

e = insert_employee(sesija, "Stojan", "mail@example.com", 30, "Developer", 60000, 2)
#e1 = insert_employee(sesija, "Bojan", "bojan@example.com", 20, "Content writer", 50000, 3)
#e1 = insert_employee(sesija, "Simona", "simona@example.com", 40, "HR", 55000, 5)


def insert_product(sesija, name, price):
    prod1 = Product(name=name, price=price)
    sesija.add(prod1)
    sesija.commit()
    print(f"Produktot {name} e dodaden")
    return prod1


def insert_sale(sesija, employee_id, product_id):
    sale1 = Sale(employee_id=employee_id, product_id=product_id)
    sesija.add(sale1)
    sesija.commit()
    print("Prodazbata e zabelezana")
    return sale1


p = insert_product(sesija, "banani", "100")
s = insert_sale(sesija, 2, 3)

"""s = Sale(employee_id=1, product_id=1)
sesija.add(s)
sesija.commit()"""

