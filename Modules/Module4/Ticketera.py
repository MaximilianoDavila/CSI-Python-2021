print("Welcome to the concert Miss World")
print("The cost of each seat follow: The principal seat = $350, the superior seat = $75, the club seat = $350")
Theprincipalseat = int(input('How many tickets sold for principal seat = '))
thesuperiorseat = int(input("How many tickets sold for superior seat = "))
theclubseat = int(input("How many tickets sold for club seat = "))

def Concertsales(Theprincipalseat, thesuperiorseat, theclubseat):
 print(f"The cost for principle seats is: {int(Theprincipalseat) * 350}")
 print(f"The cost for superior seats is: {int(thesuperiorseat) * 75}")
 print(f"The cost for club seats is: {int(theclubseat) * 350}")
print()
Concertsales(Theprincipalseat, thesuperiorseat, theclubseat)
Sales_PS = Theprincipalseat * 350
Sales_SS = thesuperiorseat * 75 
Sales_CS = theclubseat * 350
def Ticketsintotal(Sales_PS, Sales_SS, Sales_CS):
 print(f"The total of tickets sales is: ${int(Sales_PS) + int(Sales_SS) + int(Sales_CS)}")
 print()
Ticketsintotal(Sales_PS, Sales_SS, Sales_CS)