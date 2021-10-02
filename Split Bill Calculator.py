ppl = int(input("Enter the number of people: "))
print()

tax = eval(input("Enter tax amount in percentage (for example 10): "))
service = eval(input("Enter service charge in percentage (for example 5): "))
print()

tax = tax / 100
service = service / 100
           
for i in range(ppl):
    name= input("Enter the name of person: ")
    print("<Enter 'done' on meal name to exit.>")
    j = 0
    bill = 0
    while j>= 0:
        meal = input("Enter the meal/drink name: ")
        if meal == "done":
            break
        amount = eval(input("Enter the meal/drink price: "))
        bill += amount
        j+=1
    subtotal = bill + bill*tax
    total = subtotal + subtotal*service
    print("Total amount for", name, "=", '{:.2f}'.format(total))
    print("\n")
print("That's All!", "\n", "Please pay your bill accordingly.", sep="")
input("Click Enter to exit")
