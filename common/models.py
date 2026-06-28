# from pydantic import BaseModel
# from typing import List
import collections
from random import shuffle

Card = collections.namedtuple("Card", ['rank','suit'])

class Deck:

    ranks = [i for i in range(6,11)] + ['J','Q','K','A']
    suits = ["Червы","Бубны","Трефы","Пики"]

    def __init__(self):
        '''
        Инициализация колоды карт.
        '''
        self._beaten: list[Card] = []
        self._cards = [Card(rank, suit) for suit in self.suits 
                                       for rank in self.ranks]
        shuffle(self._cards)

    def __len__(self):
        '''
        Длина колоды карт.
        '''
        return len(self._cards)
    
    def __getitem__(self, pos):
        '''
        Возвращает элемент по pos из колоды карт.
        '''
        try:
            return self._cards[pos]
        except IndexError:
            return None
        
    def give_card_to_player(self, pl:Player):
        try:
            pl.hand.append(self._cards.pop())
            
        except IndexError:
            return

class Player:
    def __init__(self):
        self.hand: list[Card] = []

    def __str__(self):
        return str(self.hand)

    def __len__(self):
        return len(self.hand)

    def __getitem__(self, pos):
        '''
        Возвращает элемент по pos из руки игрока.
        '''
        try:
            return str(self.hand[pos].rank) + " " + str(self.hand[pos].suit)
        except IndexError:
            return None
    

    def take_card(self, card:Card):
        """
        Взятие карты игроком
        """
        self.hand.append(card)

    

    

a = Deck()
p = Player()
print(len(a))

for i in range(6):
    a.give_card_to_player(p)
print(len(a))
print(p)



