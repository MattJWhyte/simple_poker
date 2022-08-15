

class PokerPlayer:

    def opening_move(self, number, minimum, balance):
        return minimum

    '''
    
    e.g. arguments : 6, [10], 100, 90
    
    :returns amount to be bet, or None for fold. Two scenarios are possible:
        1) The returned amount equals the last number in history (e.g. history[-1]). This is a call, and the game ends.
        2) The returned amount is more than the last number in history. This is a raise and the game continues.
            NOTE : The amount cannot exceed opp_balance.
    '''
    def move(self, number, bets, balance, opp_balance):
        return min(1, balance, opp_balance)

    def handle_outcome(self, number, opp_number, bets, last_move, won):
        pass


