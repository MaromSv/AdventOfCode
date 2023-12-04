########NOT My Solution!################: https://topaz.github.io/paste/#XQAAAQBJBQAAAAAAAAAzHIoib6pcwaKIDwM3GRf/Gyhimru2WHGADXvOwcfrVNym3LqnqrFiuQFUkmV7qjC77TKzomxp/8XW3x5hkgQ1wE2tCuUqU+jXyFMAPYEC4qsA9hBnCcMvGY7q0HHzPVjnC2XKIcd7JN/xTKcPLEjOTqTOZHN2Rw4QbgzTYqb6y2Iz5hmuKIwyo7zn2/m3NEDbr/3p7OyPkE1uS9VhfYgJipTTFNyRkB1kZxxx6QaunBo9SdTcd5cRNk2v7KIpVbts6md35p0Eapm9bYQm7jtF0tmBh/Vbel9el+0Wwf/668ypYps4M2IWagxV8hleK4AohE5NbTbetWYm4kWBXCKOjbEG57CQsXks1VVpQc+MIauTn9OJn64P/cAPb6nfpAzgFhnp+2tzdqvq0izFuL3yN9ICjNH2FK41fLIZOTC6+GelRcqdYOJCRDy7LWjVJVSUj3ofkWKQmqSQjrUFKqyhDg1Zssm2pYkEdwtyWwcyUp+A5HSMNANH5FE3Pd/71YEB4ZuYQYymAK0nMs85ve6VURGysA7i8THVaW4PJLtiaX8nj0FlKd/Zt/jz/FSxvW13LYRH0+hq8oUmsTMadbsuYuK53KwsCuFkvpd7TBzfMIJEwsf4vWwX165PCcSeusUO+6THpfpGRlr5nuH5HyHQD0DVf1vYzIZWqR1gCbBWC3UyIPZa8ryQMdM7xOx5UBrD/wOnlx0UbJAVSvTh7Xj2qjFCuvMIUmS6P3lc0mCD3Djiuljb9BocvFwpuqrY/s1XxvWjckkMhKMZlwFcvmY7/51I1sA=


from dataclasses import dataclass


@dataclass
class LotteryCard:
    id: int
    winning_numbers: set[int]
    my_numbers: set[int]

    @property
    def wins(self):
        return self.my_numbers.intersection(self.winning_numbers)

    @property
    def value(self):
        return 2 ** (len(self.wins) - 1) if self.wins else 0

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self + other


with open("2023\day4\input.txt", "r") as f:
    data = f.read().split("\n")


def parse_card(s: str) -> LotteryCard:
    card_id, card_numbers = s.split(":")
    winning_numbers, my_numbers = card_numbers.strip().split(" | ")

    return LotteryCard(
        id=int(card_id.strip().split("Card ")[1].strip()),
        winning_numbers={
            int(n.strip()) for n in winning_numbers.strip().split(" ") if n
        },
        my_numbers={int(n.strip()) for n in my_numbers.strip().split(" ") if n},
    )


cards = list(map(parse_card, data))

print("Part I Solution:", sum(cards))


## Dynamic programming for II
memo = {}

for card in cards[::-1]:
    new_cards_won = cards[card.id : (card.id + len(card.wins))]
    children_values = sum([memo[c.id] for c in new_cards_won])
    memo[card.id] = len(new_cards_won) + children_values


print("Part II Solution:", len(cards) + sum(memo.values()))