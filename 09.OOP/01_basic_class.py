
# class Employee {
#   constructor(private name: string) {}

#   setName(newName: string): void {
#     this.name = newName
#   }

#   setSalary(salary: number): void {
#     this.salary = salary
#   }

#   giveRaise(amount: number): void {
#     this.salary += amount
#   }
# }

class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
	
  def set_salary(self, new_salary):
    self.salary = new_salary 

  def give_raise(self, amount):
    self.salary += amount

emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.name)
print(emp.salary)

emp.give_raise(10000)
print(emp.salary)

