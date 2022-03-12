# Blind Auction 💰
# https://replit.com/@ArgemFlores/blind-auction

# import libraries
from replit import clear
import art

# initialize bid variables
more_bids = 'yes'
bids = {}

# ask for inputs repeatedly until no
while more_bids == 'yes':
    clear()

    # print logo
    print(art.logo)
    print("The Blind Auction 💰\n")

    # prompt name and bid
    name = input("👤 What is your name? ")
    bid = input("💵 What is your bid? $")

    # invalid bid if not numeric or empty
    if not bid.isnumeric() or int(bid) <= 0:
        # ask to try again or not
        more_bids = input(f"\n❌ Invalid bid amount '{bid}'. Try again? yes/no: ")

        # try again
        if more_bids == 'yes':
            continue
        else:
            # exit loop
            clear()
            break

    # convert bid to float
    bids[name] = float(bid)

    # ask to enter more or exit loop
    more_bids = input("\n✅ Bid entered! Are there any other bidders? yes/no: ").lower()

# initialize winning variables
winning_bidders = []
winning_bid = 0

# find the highest bidder
for name, bid in bids.items():
    # current bid exceeds current winning bid
    if bid >= winning_bid:
        # set as current winning bid and bidder/s
        winning_bid = bid
        winning_bidders.append(name)

# clear screen
clear()

# print logo
print(art.logo)

# winner found
if winning_bid > 0:
    # print winning bid and bidder/s
    print(f"🙋 The winning bid is ${winning_bid:.2f} from {', '.join(winning_bidders)}. Congratulations! 😄")
else:
    # winner not found because there are no valid bids
    print(f"🤷 No valid bids were entered. Thanks for trying! 🙂")
