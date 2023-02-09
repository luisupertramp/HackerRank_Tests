def towerBreakers(n, m):
    # NOTE: I really like this challenge because of its simplicity at solving, but it's complexity at understanding...
    # NOTE: ... what is the problem asking for.

    # If the towers are only 1 level high, there is nothing the Player 1 can do so P2 wins
    if m == 1 : 
        return 2

    # otherwise it all depends on the amount of towers, not the amount of levels
    else:
        if n % 2 == 0 :
            return 2
        else :
            return 1

# print(towerBreakers(10000, 1))
# print(towerBreakers(2, 4))
# print(towerBreakers(1, 4))