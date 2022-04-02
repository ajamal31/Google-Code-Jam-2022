n = int(input())

for i in range(n):
    r, c = map(int, input().split())
    print(f'Case #{i + 1}:')
    print(f'..{"+-" * (c - 1)}+') 
    print(f'..{"|." * (c - 1)}|') 
    for _ in range(r - 1):
        print(f'{"+-" * c}+') 
        print(f'{"|." * c}|') 
    print(f'{"+-" * c}+') 