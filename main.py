import utils as util
from models import Company


def main():
    print("Hello World!")
    print("Downloading prices.")

    try:
        amount = int(input("Please add amount to invest: "))
        no_companies = int(input("Please add number of companies from the index to copy(1-17): "))
    except ValueError:
        print("Values need to be integers!")

    bet_index = util.get_BET_index(no_companies)
    bet_index = rebalance(bet_index)
    calculate_no_of_shares(amount, bet_index)

    print("Allocation:")
    total = 0

    for i in range(0, len(bet_index)):
        print(
            f'{bet_index[i].name:50} {bet_index[i].symbol:5} ==> {bet_index[i].no_shares:6} @{bet_index[i].price} = {bet_index[i].no_shares * bet_index[i].price}')
        total += bet_index[i].no_shares * bet_index[i].price

    print("Total invested: " + str(total))


def calculate_no_of_shares(amount, bet_index):
    for i in range(0, len(bet_index)):
        bet_index[i].no_shares = (amount * (bet_index[i].new_weight / 100)) // bet_index[i].price
    return bet_index


def rebalance(bet_index):
    total_perc = 0

    for i in range(0, len(bet_index)):
        total_perc += bet_index[i].weight
    for i in range(0, len(bet_index)):
        bet_index[i].new_weight = (bet_index[i].weight * 100) / total_perc

    return bet_index


if __name__ == "__main__":
    main()
