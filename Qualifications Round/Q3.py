n = int(input())

for i in range(n):
    num_of_dices = int(input())
    dices = [*map(int, input().split())]
    dices.sort()

    answer = 0
    count = 0
    for j in range(len(dices)):
        if answer < dices[j]:
            answer += 1

    print(f'Case #{i + 1}: {answer}')