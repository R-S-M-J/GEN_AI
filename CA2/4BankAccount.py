class BankAcc:
    def __init__(self, accNo, intR8):                   # intizlize with acount number, interest rate.
        self.accNo = accNo
        self.intR8 = intR8
        self.t = []                                     # transaction list to store expenditure for each month

    def add(self, m, amt):
        if amt < 0 and self.balance() + amt < 0:
            print(f"Insufficient funds for withdrawal. Withdrawl of Rs {-amt} rejected")
            return
        if m < 1 or m > 6:
            print(f"Month must be between 1 and 6. Process terminated for month {m}")
            return
        if len(self.t) < m:
            self.t.extend([[] for _ in range(m - len(self.t))])
        
        self.t[m - 1].append(amt)

    def minBal(self):
        c = []
        if not self.t:
            print("No Transactions")
            c.append(0)                                 # exmpty transactions list means no balance
        else:
            for i in self.t:
                b = 0
                l1 = []
                for t in i:
                    b += t
                    l1.append(b)
                if l1:
                    c.append(min(l1))
                
        return c
    
    def balance(self):
        total = 0
        for month in self.t:
            total += sum(month)
        return total

    def interest(self):
        c = self.minBal()
        tc = sum(c)
        ti = tc * (self.intR8 / 100)
        mi = ti / 12
        r = max(0, mi * 6)                              # interest remains non-negative
        return r

acc = BankAcc("123456", intR8=4.5)

# positive to deposit
# negative to withdraw
acc.add(1, 1000)
acc.add(7, -200)
acc.add(2, 500) 
acc.add(3, -200)

interest = acc.interest()
print(f"Interest for 6 months: {interest}")
