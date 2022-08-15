

from poker_player import PokerPlayer

from random import randint

class SimplePoker:

    def __init__(self, initial_balance, minimum_opening, p1, p2):
        self.initial_balance = initial_balance
        self.minimum_opening = minimum_opening
        self.players = [p1, p2]
        self.wins = [0,0]

    def alea_iacta_est(self):
        score1 = randint(0,9)
        score2 = randint(0,9)
        while score1 == score2:
            score2 = randint(0, 9)
        if randint(0,1) == 0:
            return score1, score2
        return score2, score1

    def play_game(self, p1_first=False, verbose=True):
        s = self.alea_iacta_est()
        n = 0
        offset = 0 if p1_first else 1
        balances = [self.initial_balance] * 2

        # Args : number, minimum, balance
        bets = [self.players[offset].opening_move(s[offset], self.minimum_opening, self.initial_balance)]

        # Check for violations
        if bets[-1] < self.minimum_opening:
            print("PLAYER {} BET ({}), BELOW MINIMUM OPENING ({})".format(offset+1, bets[-1], self.minimum_opening))
            if verbose:
                print("Player {} wins".format(2-offset))
                print("-------------------------")
            return 1 - offset
        if bets[-1] > self.initial_balance:
            print("PLAYER {} BET ({}), EXCEEDING INITIAL BALANCE ({})".format(offset+1, bets[-1], self.initial_balance))
            if verbose:
                print("Player {} wins".format(2-offset))
                print("-------------------------")
            return 1 - offset

        if verbose:
            print("Player 1 has {}".format(s[0]))
            print("Player 2 has {}".format(s[1]))
            print("-------------------------")
            print("Player {} bet {}".format(offset+1, bets[-1]))

        # Check for fold or
        winner = None

        while winner is None:
            n += 1
            # i = 0 if p1 and i = 1 if p2
            i = (n + offset) % 2
            # args : number, bets, balance, opp_balance
            bets.append(self.players[i].move(s[i], bets, balances[i], balances[1-i]))

            if bets[-1] is None: # Current player has folded
                # Notify p1 of outcome
                # Notify p2 of outcome
                winner = 1-i  # Opposite player won
                if verbose:
                    print("Player {} folded".format(i + 1))
            elif bets[-1] == bets[-2]: # Call
                winner = i if (s[i] > s[1-i]) else 1-i
                if verbose:
                    print("Player {} bet {} (Call)".format(i + 1, bets[-1]))
            elif bets[-1] > bets[-2]: # Raise
                if verbose:
                    print("Player {} bet {} (Raise)".format(i + 1, bets[-1]))
                if bets[-1] > balances[i]:
                    print("PLAYER {} EXCEEDED THEIR BALANCE".format(i+1))
                    winner = 1-i
                elif bets[-1] > balances[1-i]:
                    print("PLAYER {} EXCEEDED OPPONENT BALANCE".format(i+1))
                    winner = 1-i
                else: # Game continues
                    balances[i] = self.initial_balance - bets[-1]

        i = (n + offset) % 2
        # Loop terminates as there is a winner
        # args : number, opp_number, bets, last_move, won
        self.players[0].handle_outcome(s[0], s[1], bets, (i == 0), (winner == 0))
        self.players[1].handle_outcome(s[1], s[0], bets, (i == 1), (winner == 1))

        if verbose:
            print("Player {} wins".format(i + 1))
            print("-------------------------")

        return winner





