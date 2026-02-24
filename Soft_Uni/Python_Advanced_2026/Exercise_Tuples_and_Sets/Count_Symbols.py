text = input()

unique_symbols = set()

for char in text:
    unique_symbols.add(char)

for symbol in sorted(unique_symbols):
    print(f"{symbol}: {text.count(symbol)} time/s")