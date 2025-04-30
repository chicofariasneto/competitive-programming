t = int(input())
for _ in range(t):
    numbers = list(map(int, input().split()))
    print('YES'
          if min(numbers[0], numbers[1]) < max(numbers[2], numbers[3])
             and min(numbers[2], numbers[3]) < max(numbers[0], numbers[1])
          else 'NO')