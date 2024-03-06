n = int(input())
birthdays = {}

for _ in range(n):
    name, day, month = input().split()
    if month not in birthdays:
        birthdays[month] = []
    birthdays[month].append(name)

requested_month = input()

if requested_month in birthdays:
    names = birthdays[requested_month]
    print(*names)
else:
    print()