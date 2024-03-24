janken_num = int(input())
win = 0
lose = 0
draw = 0
for i in range(janken_num):
    card = input()
    p1 = card[:card.find(" ")]
    p2 = card[card.find(" ") + 1:]
    if p1 == "G":
        if p2 == "P":
            lose += 1
        if p2 == "C":
            win += 1
        if p2 == "G":
            draw += 1
    if p1 == "P":
        if p2 == "C":
            lose += 1
        if p2 == "G":
            win += 1
        if p2 == "P":
            draw += 1
    if p1 == "C":
        if p2 == "G":
            lose += 1
        if p2 == "P":
            win += 1
        if p2 == "C":
            draw += 1
print(win)