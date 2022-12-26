### Read CSV bank or credit card statements, assign catagory to the expense, and compute individual expense

import csv

destination = input('Enter destination file name: ')
if len(destination) < 1: destination = 'exp.csv'

# Write the title row to the new csv file
with open(destination, 'a') as new_file:
    writer_obj = csv.writer(new_file)
    header = ('Date','Description','Amount','Catagory')
    writer_obj.writerow(header)

#read the current csv file
source_name = input('Enter source file name: ')

with open(source_name, mode="r") as source_file:
    reader_obj = csv.reader(source_file)
#open the destination csv file
    with open(destination, 'a') as new_file:
        writer_obj = csv.writer(new_file)
# loop through to read the data
        for row in reader_obj:
            date = row[1]
            description = row[2]
            amount = row[3]
            catagory = ''
# If the row does not have numeric expense skip
            try:
                amount = float(amount)
            except:
                continue
# If catagory is recognized assign the description
            Dict = {'JACK':'Rent', 'Salvador':'Gardening', 'LADWP':'Utility', 'Treasurer':'Property Tax','Juan':'Repair','Armando':'Repair','Marco':'Repair'}
            for d_key in Dict:
                if d_key in description:
                    catagory = Dict[d_key]
                else: continue

            tup = (date, description, amount, catagory)
# Writes to the destination CSV file
            writer_obj.writerow(tup)


# Read through catagorized file and compute sum of each catagory
with open(destination, mode='r') as source_file:
    reader_obj = csv.reader(source_file)

    sum = 0

    Dict_sum = {'Rent':0, 'Gardening':0, 'Repair':0, 'Utility':0, 'Property Tax':0}

    for row in reader_obj:
        catagory = row[3]
        amount = row[2]
        try:
            amount = float(amount)
        except:
            continue

        sum = sum + amount

        for r_key in Dict_sum:
            if r_key == catagory:
                Dict_sum[r_key] = Dict_sum[r_key] + amount

#Write the sum of each catagory to the .csv file
data = [
    ['Total', sum],
    ['Rent', Dict_sum['Rent']],
    ['Gardeing', Dict_sum['Gardening']],
    ['Repair', Dict_sum['Repair']],
    ['Utility', Dict_sum['Utility']],
    ['Property Tax', Dict_sum['Property Tax']]
    ]

with open(destination, 'a') as new_file:
    writer_obj = csv.writer(new_file)
    for item in data:
        writer_obj.writerow(item)
