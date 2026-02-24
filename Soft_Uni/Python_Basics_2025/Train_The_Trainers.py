judges = int(input())
presentation_name = input()
total_score = 0
total_presentations = 0

while presentation_name != "Finish":
    total_score_presentation = 0

    for i in range(judges):
        score = float(input())
        total_score_presentation += score
        total_score += score

    avarage_score_presentation = total_score_presentation / judges
    print(f"{presentation_name} - {avarage_score_presentation:.2f}.")

    total_presentations += 1
    presentation_name = input()

avarage_score = total_score / (total_presentations * judges)
print(f"Student's final assessment is {avarage_score:.2f}.")