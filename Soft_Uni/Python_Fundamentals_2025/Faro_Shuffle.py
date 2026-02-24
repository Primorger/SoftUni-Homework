deck = input().split()
n = int(input())

for current_shuffle in range(n):
    deck_middle = len(deck) // 2

    deck_1 = deck[:deck_middle]
    deck_2 = deck[deck_middle:]

    final_deck = []

    for card_index in range(len(deck_1)):
        final_deck.append(deck_1[card_index])
        final_deck.append(deck_2[card_index])
        
    deck = final_deck.copy()

print(final_deck)