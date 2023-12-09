a = int(input("int : "))
m = []
for A in range(0 , a):
    b = int(input(f"input {A + 1} : "))
    m.append(b)
H = 0
for total in m:
    H = H + total

I = 1
for beat in m:
    I = I * beat

Max_is = []
for MAX in range(1 , H):
    for max in range(1 , a):
        Max = m[max - 1]
        if Max == MAX:
            Max_is.append(Max)

Min_is = []
for MIN in range(H , 0 , -1):
    for min in range(a , 0 , -1):
        Min = m[min - 1]
        if Min == MIN:
            Min_is.append(Min)

Avg_is = []
h = 1
for AVG in m:
    h = h +AVG
    Avg_is.append(h)
h = int(h / len(Avg_is))

if len(m) % 2 !=0:
    Mean_is = m[int(len(m) / 1.5) - 2]
if len(m) % 2 ==0:
    Mean_1 = m[int(len(m) / 2)]
    Mean_2 = Mean_1 + 1
    Mean_is = Mean_1 + Mean_2
    Mean_is = int(Mean_is / 2)

Last_three_numbers_are_is = []
for last_three_numbers_are in range(len(m) - 3 , len(m)):
    Last_three_numbers_are_is.append(m[last_three_numbers_are])

Two_numbers_with_highest_count_are = []
for TWO_NUMBERS_WITH_HIGHEST_COUNT_ARE in m:
    count = 0
    if TWO_NUMBERS_WITH_HIGHEST_COUNT_ARE not in list(map(lambda w: w[0] , Two_numbers_with_highest_count_are)):
        for two_numbers_with_highest_count_are in m:
            if TWO_NUMBERS_WITH_HIGHEST_COUNT_ARE == two_numbers_with_highest_count_are:
                count += 1
        Two_numbers_with_highest_count_are.append((TWO_NUMBERS_WITH_HIGHEST_COUNT_ARE , count))

Two_numbers_with_highest_count_are.sort(key=lambda p: -1 * p[1])

print()
print(f"Max is {int(Max_is[len(Max_is) - 1])}")
print(f"Min is {int(Min_is[len(Min_is) - 1])}")
print(f"Avg is {h}")
print(f"Mean is {Mean_is}")
print(f"Last three numbers are {Last_three_numbers_are_is}")
print(f"Two numbers with highest count are {Two_numbers_with_highest_count_are[0]} and {Two_numbers_with_highest_count_are[1]}") 
print(f"Sum of all is {H}")
print(f"Product of all is {I}")