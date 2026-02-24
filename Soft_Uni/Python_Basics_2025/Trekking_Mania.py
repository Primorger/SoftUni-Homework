# · Първи ред - процентът изкачващи Мусала
# · Втори ред – процентът изкачващи Монблан
# · Трети ред – процентът изкачващи Килиманджаро
# · Четвърти ред – процентът изкачващи К2
# # · Пети ред – процентът изкачващи Еверест

groups = int(input())

musala = 0
montblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
group_size = 0
tot_people = 0

for _ in range(groups):
    group_size = int(input())
    tot_people += group_size
    if group_size <= 5:
        musala += group_size
    elif 6 <= group_size <= 12:
        montblan += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro += group_size
    elif 26 <= group_size <= 40: 
        k2 += group_size
    elif group_size >= 41:
        everest += group_size

musala_prosentage = musala / tot_people * 100
montblan_prosentage = montblan / tot_people * 100
kilimanjaro_prosentage = kilimanjaro / tot_people * 100
k2_prosentage = k2 / tot_people * 100
everest_prosentage = everest / tot_people * 100

print(f"{musala_prosentage:.2f}%")
print(f"{montblan_prosentage:.2f}%")
print(f"{kilimanjaro_prosentage:.2f}%")
print(f"{k2_prosentage:.2f}%")
print(f"{everest_prosentage:.2f}%")