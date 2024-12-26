P = int(input())
N = int(input())
R = int(input())

total_infected = 0
infected_today = N
day = 0

while total_infected <= P:
    total_infected += infected_today
    day += 1
    if total_infected > P:
        print(day-1)
        break
    infected_today *= R