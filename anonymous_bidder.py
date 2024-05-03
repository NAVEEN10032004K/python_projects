logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

from replit import clear

bid = {}

truth_value = True

def highest_bidder(bid):
    highest_bid = 0
    winner = ""
    for bidder in bid:
        bid_amount = bid[bidder]
        bid_amount = int(bid_amount)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while truth_value:
    name = input("What's your name? ")
    amount = input("What's your bid: $")
    bid[name] = amount
    other_bidder = input("Is there any other bidder? ")
    if other_bidder == "yes":
        clear()
    elif other_bidder == "no":
        truth_value = False


highest_bidder(bid)
