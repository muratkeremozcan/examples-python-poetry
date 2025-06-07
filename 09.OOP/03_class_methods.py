# Class methods are bound to the class, not the instance: 
## they receive the class (cls) as their first argument instead of the instance (self).
# Alternative constructors: Often used to create factory methods that return class instance
# They can be used to enforce restrictions on instance creation (singleton - db connections or config come to mind)

class Person:
	CURRENT_YEAR = 2025
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def from_birth_year(cls, name, birth_year):
		age = Person.CURRENT_YEAR - birth_year
		return cls(name, age)

p1 = Person("John", 30)
p2 = Person.from_birth_year("John", 1990)

print(p1.age)
print(p2.age)

# class Person {
#     static CURRENT_YEAR = 2025;
    
#     constructor(public name: string, public age: number) {}
    
#     // Static factory method (TypeScript's equivalent to @classmethod)
#     static fromBirthYear(name: string, birthYear: number): Person {
#         const age = Person.CURRENT_YEAR - birthYear;
#         return new Person(name, age);
#     }
# }

# const p1 = new Person("John", 30);
# const p2 = Person.fromBirthYear("John", 1990);

class BetterDate:
	def __init__(self, year, month, day):
		self.year, self.month, self.day = year, month, day

	@classmethod
	def from_str(cls, datestr):
		parts = datestr.split('-')
		year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
		# year, month, day = map(int, datestr.split('-')) # better way
		return cls(year, month, day)

xmas = BetterDate.from_str("2025-12-25")
print(xmas.year, xmas.month, xmas.day)

# class BetterDate {
#     constructor(
#         public year: number,
#         public month: number,
#         public day: number
#     ) {}

#     // Static factory method using array destructuring
#     static fromStr(dateStr: string): BetterDate {
#         const [year, month, day] = dateStr.split('-').map(Number);
#         return new BetterDate(year, month, day);
#     }
# }

# // Usage
# const xmas = BetterDate.fromStr("2025-12-25");
# console.log(xmas.year, xmas.month, xmas.day);