def conversion():
    amount = input("Please specify the amount: ")
    assert (amount > 0),"please enter a positive value!"
    assert (amount > 100),"please enter a value greater than 100!"
    answer = raw_input("Please choose between converting FROM kilograms/pounds: ")
    if answer == "kilograms":
        return (amount * 2.2, "pounds")
    elif answer == "pounds":
        return (amount / 2.2, "kilograms")
    else:
        print "Please choose between kilograms and pounds."
        restart = raw_input("Try again? ")
        if restart == "yes":
            conversion()
            return 0
        elif restart == "y":
            conversion()
            return 0 
        else:
            print "Okay, bye."
            return
finalresult = conversion()
print "the final result is: ", finalresult[0], finalresult[1]
