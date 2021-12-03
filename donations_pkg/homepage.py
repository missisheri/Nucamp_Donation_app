
def show_homepage():
    print("")
    print("         === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|             5.    Exit                 |")
    print("------------------------------------------")


def donate(username):
    donate_amt = float(input("Enter amount to donate: "))
    donation = username + " donated $"+str(donate_amt)
    print(donation)
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    if not donations:
        print("currently, there are no donations")
    else:
        for donation_msg in donations:
            print(donation_msg)
