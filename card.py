class Card:

    SPECIAL_CARDS = {
        11: "Jack",
        12: "Queen",
        13: "king",
        14: "Ace"
    }

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def is_special(self):
        if self._value > 10:
            return True
        else:
            return False

    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        card_symbol = self.suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {card_symbol}")
        else:
            print(f"{card_value} of {card_suit} {card_symbol}")
