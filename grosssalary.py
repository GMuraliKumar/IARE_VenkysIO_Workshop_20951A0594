gr=float(input("Enter Gross Salary : "))
fd=float(input("Enter Federal Deduction : "))
sd=float(input("Enter State Deduction: "))
pe=float(input("Enter Pension Pecentage : "))
nw=float(input("Enter Number of Weeks : "))
tot=(fd+sd+pe)*(gr/100)
print("Total Salary : ",4*(gr-tot))
