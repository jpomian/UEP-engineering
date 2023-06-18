import csv

class Employee:
    def __init__(self, name, gross_salary):
        self.name = name
        self.gross_salary = float(gross_salary)

    def calculate_net_salary(self):
        # Niewiadomo jaki podatek wiec ustalamy na poziomie 20% i podatek od ubezpieczenia 3%. Łącznie 23% jak VAT.
        tax = 0.2 * self.gross_salary
        insurance = 0.03 * self.gross_salary
        net_salary = self.gross_salary - tax - insurance
        return round(net_salary, 2)

    def calculate_total_cost(self):
        tax = 0.2 * self.gross_salary
        insurance = 0.03 * self.gross_salary
        return round(tax+insurance, 2)

def main():
    with open('employees.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        # Pomijamy pierwszy wiersz (header)
        next(reader)
        
        for row in reader:
            emp_name, emp_gross_sal = row
            
            e = Employee(emp_name, emp_gross_sal)
            
            print(f"{e.name}: Płaca Netto = {e.calculate_net_salary()}. Koszt całkowity = {e.calculate_total_cost()}")

if __name__ == '__main__':
    main()