'''
[to52 data structure]

|              hashmap pointer (52 bits)               |
|------||------||------||------||------||------||------||------| <-----+
0000AKQJT98765432AKQJT98765432AKQJT98765432AKQJT987654320000scdh <---+ |
    |   hearts  ||  diamonds ||   clubs   ||  spades   |    suit <-+ | |
                                                                   | | |
 The playing card is represented                           [types]-+ | |
 by 7 bytes for the hashmap.                                         | |
                                                      [bit values]---+ |
 Poker hand can be obtained by combining                               |
 several cards using logical OR operation.   [byte representation]-----+
'''

class Converter(object):
    '''playing card string to integer converter'''
    def __init__(self):
        self.PRIME = {
            '2': 2, '3': 3, '4': 5, '5': 7, '6': 11, '7': 13, '8': 17,
            '9': 19, 'T': 23, 'J': 29, 'Q': 31, 'K': 37, 'A': 41
        }
        self.INT_SUIT = {}
        self.RANK = '23456789TJQKA'
        self.SUIT = 'HDCS'
        self.bitmap = {}
        
        for s in range(len(self.SUIT)):
            c_suit = 1 << s
            self.INT_SUIT[self.SUIT[s]] = c_suit
            for r in range(len(self.RANK)):
                self.bitmap[self.RANK[r] + self.SUIT[s]] = (1<<r<<s*13, c_suit)
    
    def to52(self, card):
        '''
        takes the value of a card like '2c', 'Ts', 'Kd', 'Qh', etc.
        returns card pointer and the suit.
        '''
        return self.bitmap[card.upper()]
    
    def toPrime(self, card):
        '''matches a card without a suit to a prime number'''
        card = card.upper()
        return (self.PRIME[card[0]], self.INT_SUIT[card[1]])

