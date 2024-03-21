from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print (logo)
bids = {}
bidding_finished = False

# Virtual environment notes:
#ccrow@ccrow-gentoo ~/personal/100python $ cd projects/09\ -\ dicts\ and\ nesting/
#ccrow@ccrow-gentoo ~/personal/100python/projects/09 - dicts and nesting $ python -m venv .
#ccrow@ccrow-gentoo ~/personal/100python/projects/09 - dicts and nesting $ . bin/activate

def find_highest_bid(bidding_dict):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dict:
        if bidding_dict[bidder] > highest_bid:
            highest_bid = bidding_dict[bidder]
            winner = bidder
    print (f"The winner is {winner} with a bid of ${highest_bid}")
    

while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bids[name] = bid

    again = input("Any other users want to bid? (y/n) ")
    clear()
    if again == 'n':
        find_highest_bid(bids)
        bidding_finished = True
    



