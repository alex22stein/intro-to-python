employees = []
with open("intro_python\\hr_system\\hr_system.txt") as hr_system:
    for line in hr_system:
        x = (line.split())
        employees.append(x)

for line in employees:
    paycheck = int(line[3]) / (12 * 2)
    if line[2] == "Engineer":
        paycheck = paycheck + 1000
    print(f'{line[0]} (ID:{line[1]}), {line[2]} - ${paycheck:.2f}')