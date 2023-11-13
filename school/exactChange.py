# return dictionary with coin type and count
def get_change(cents):
    quarters = int(cents // 25) # get the number of quarters
    change = cents % 25         # get the remainder of change without quarters
    dimes = int(change // 10)   # get the number of dimes
    change %= 10                # get the remainder without dimes
    nickels = int(change // 5)  # get the number of nickels
    pennies = change % 5        # get the remainder without nickels
    return {"quarters": quarters,
            "dimes": dimes,
            "nickels": nickels,
            "pennies": pennies}


change_in_cents = int(input("Enter change in cents: "))
print(get_change(change_in_cents))
