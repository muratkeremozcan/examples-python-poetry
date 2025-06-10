class BankAccount:
	def __init__(self, number, balance=0):
		self.balance = balance
		self.number = number

	def withdraw(self, amount):
		self.balance -= amount

	@classmethod
	def _is_bank_account(cls, obj) -> bool:
		  # Check that verifies if other is an instance of the same class as self
			return isinstance(obj, cls)

	# Overriding the __eq__ method
	# return True if the number attribute is the same and the type() of both objects passed to it is the same.
	def __eq__(self, other):
			if not self._is_bank_account(other):
					return NotImplemented
			return (self.number == other.number) and (self.balance == other.balance)

	def __ne__(self, other):
			if not self._is_bank_account(other):
					return NotImplemented
			return self != other

	def __lt__(self, other):
			if not self._is_bank_account(other):
					return NotImplemented
			return self.balance < other.balance

	def __le__(self, other):
			if not self._is_bank_account(other):
					return NotImplemented
			return self.balance <= other.balance

	def __gt__(self, other):	
			if not self._is_bank_account(other):
					return NotImplemented
			return self.balance > other.balance

	def __ge__(self, other):
			if not self._is_bank_account(other):
					return NotImplemented
			return self.balance >= other.balance

	# Provides a complete, unambiguous string representation of an object
	def __repr__(self):
			return f"BankAccount(number={self.number}, balance={self.balance})"


acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)



class Phone:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
         return (self.number == other.number) and (type(self) == type(other))

pn = Phone(873555333)
acct4 = BankAccount(873555333)
print(pn == acct4)

# class BankAccount {
#   constructor(
#     public readonly number: number, 
#     private _balance: number = 0
#   ) {}

#   withdraw = (amount: number): void => { this._balance -= amount; }
#   get balance(): number { return this._balance; }

#   private static isBankAccount = (obj: any): obj is BankAccount => 
#     obj instanceof BankAccount;

#   equals = (other: unknown): boolean => 
#     BankAccount.isBankAccount(other) && 
#     this.number === other.number && 
#     this._balance === other._balance;

#   notEquals = (other: unknown): boolean => !this.equals(other);
#   lessThan = (other: BankAccount): boolean => this._balance < other._balance;
#   lessThanOrEqual = (other: BankAccount): boolean => this._balance <= other._balance;
#   greaterThan = (other: BankAccount): boolean => this._balance > other._balance;
#   greaterThanOrEqual = (other: BankAccount): boolean => this._balance >= other._balance;
#   toString = (): string => [BankAccount(number=${this.number}, balance=${this._balance})];
# }

# // Example usage
# const [acct1, acct2, acct3] = [
#   new BankAccount(123, 1000),
#   new BankAccount(123, 1000),
#   new BankAccount(456, 2000)
# ];

# console.log(acct1.equals(acct2));  // true
# console.log(acct1.notEquals(acct3)); // true
# console.log(acct1.lessThan(acct3)); // true

# // Phone class example
# class Phone {
#   constructor(public number: number) {}
#   equals = (other: unknown): boolean => 
#     other instanceof Phone && this.number === other.number;
# }

# console.log(acct1.equals(new Phone(123)));  // false