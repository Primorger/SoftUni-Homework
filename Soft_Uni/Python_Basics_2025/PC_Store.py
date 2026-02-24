# •	На първи ред: цената в долари за процесора – реално число в интервала [200.00 … 3000.00]
processor_price = float(input())
# •	На втори ред: цената в долари за видео карта – реално число в интервала [100.00 … 1500.00]
video_card_price = float(input())
# •	На трети ред: цената в долари за една RAM памет – реално число в интервала [80.00 ... 500.00]
ram_price = float(input())
# •	На четвърти: ред брой RAM памети – цяло число в интервала [1 ... 4]
ram_quantity = int(input())
# •   На пети ред: процент отстъпка – реално число в интервала [0.01 … 0.1]
discount = float(input())
leva_conversion_rate = 1.57

processor_price = (processor_price * leva_conversion_rate) * (1 - discount)
video_card_price = (video_card_price * leva_conversion_rate) * (1 - discount)
ram_price = (ram_price * leva_conversion_rate) * ram_quantity
tot_price = processor_price + video_card_price + ram_price

print(f"Money needed - {tot_price:.2f} leva.")
