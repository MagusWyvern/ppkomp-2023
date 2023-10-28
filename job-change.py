'''
Muhammad Dhaifullah has taken a Diploma in Information Technology (Digital Technology) course at Politeknik Mersing. After finishing his studies, he worked in a local company near his home.

When receiving his first job offer, Muhammad Dhaifullah didn't care much about the salary offered as this was his first career and he just wanted to gain work experience. While working, he also applied for vacancies in other companies.

Several companies have offered him positions at different times. So he intends to accept any offer that reaches him first on the condition that the salary offered in the new company is more than RM200 compared to the current salary.

After getting a new job, he will repeat the same thing to make sure he gets a higher salary.

Given a list of integers, representing the salaries offered to Muhammad Dhaifullah in chronological order. You are to determine which salary offers he will accept in chronological order.

# Sample case 1:

# Sample input 1:
1400, 1350, 1500, 1600, 1750, 1500, 1800, 1980, 2100, 2250, 1800, 2300

# Sample output 1:
1400, 1750, 1980, 2250

In his first job, he earned a salary of RM1400.
He changed jobs for the first time when he was offered a salary of RM1750.
He changed jobs for the second time when he was offered a salary of RM1980.
He changed jobs for the third time when he was offered a salary of RM2250.
'''

salaries = list(map(int, input().split(", ")))

current_salary = salaries[0]

accepted_salaries = [salaries[0]]

# Check if the salary offered is more than RM200 compared to the current salary
# If yes, accept the offer and change the current salary to the new salary

# Repeat the same process for the next salary offered
# Add the accepted salary to list 'accepted_salaries'

for i in range(1, len(salaries)):
    if salaries[i] > current_salary + 200:
        accepted_salaries.append(salaries[i])
        current_salary = salaries[i]

# Print the accepted salaries in chronological order, separated by commas

print(", ".join(map(str, accepted_salaries)))