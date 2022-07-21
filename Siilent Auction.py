import logo
#key is the name and the bid is he value
logo = logo.logo
print(logo)
print("Welcome to the secret auction program")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_records):
    highest_bid = 0
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    bid_price = int(input("what is your bid? $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? 'yes' or 'no'\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()


