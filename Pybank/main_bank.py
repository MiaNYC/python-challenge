import os
import csv
dir_path = os.path.dirname(os.path.realpath(__file__))
bank_csv_path = os.path.join(dir_path, '03-Python_homework_assignment_PyBank_Resources_budget_data.csv')
months = []
net_revenue = 0


with open(bank_csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #print(row) 
        months.append(row)
        net_revenue = net_revenue + int(row[1])

# print ("months", str(months))
month, amount = map(list, zip(*months))
# print("final lists", month, "\n", amount) 
amount_month = list(zip(amount, month))
sorted_months = sorted(amount_month)
amount = sorted(amount)
# print(sorted_months[0])
# print(sorted_months[-1])

print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {len(months)}")
#print("There are " + str(len(months)) + " months")
# print(months[0])
print(f"Total: ${net_revenue}")
# print(net_revenue)
# print(sorted_months)
# print(amount)
