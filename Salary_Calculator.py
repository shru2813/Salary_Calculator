workHours = []
total_days=0
salary = 0
for i in range(7):
    workHours.append(int(input("enter hrs for a day:")))
    total_days += workHours[i]
    salary += (workHours[i] * 100)
    if workHours[i] > 8:
        salary += (workHours[i] % 8) * 15
if workHours[0]:
    salary += (workHours[0] * 100) * 0.5
if workHours[6]:
    salary += (workHours[6] * 100) * 0.25
if total_days > 40:
    salary += (total_days-40) * 25
print(salary)
