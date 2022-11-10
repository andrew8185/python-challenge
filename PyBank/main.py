#import modules
import os
import csv

#notate the path to the csv
csvpath = os.path.join("Resources", "budget_data.csv")

#open the csv file being used
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header in the csv file
    csv_header = next(csvreader)
    #define initial variables as open lists
    Total_months = []
    total = []
    pl_difference = []

    #setting up the overarching 'for' loop
    for row in csvreader:
        
        #The entire column of months from the csv file appended to the Total_months open list
        Total_months.append(row[0])
    
        #The entire column of profit and losses from the csv appended to the total open list
        total.append(int(row[1]))
    
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #loop through the list of total values, starting at 1. 
    #Append the difference of the next cell minus the current cell to the pl_difference list
    for x in range(1,len(total)):
        pl_difference.append(int(total[x])-int(total[x-1])) 
    
    #adding up the newly created pl_difference list divided by the total number of months in (Total_months - 1) using len()
    avg_pl = sum(pl_difference)/(len(Total_months)-1)
    
    #using the min/max functions on the pl_difference list
    greatest_increase = max(pl_difference)
    greatest_decrease = min(pl_difference)
    
    #find the row index integer value of min/max values in the entire list of p & l values
    max_month_index = int(pl_difference.index(greatest_increase))
    min_month_index = int(pl_difference.index(greatest_decrease))

#print output to terminal along with writing to a new .txt file
save_to = os.path.join("resources","Financial_analysis.txt")

with open(save_to,"w") as txt_file:   
    print("Financial Analysis")
    txt_file.write("Financial Analysis")
    print("-------------------------------------------")
    txt_file.write(f'\n-------------------------------------------')
    
    #printing the length of the total month column to get the total number of months
    print(f"Total Months: {len(Total_months)}")
    txt_file.write(f'\nTotal Months: {len(Total_months)}')
    
    #using the sum function to get the total profit and loss over the entire period
    print(f"Total: ${sum(total)}")
    txt_file.write(f'\nTotal: ${sum(total)}')
    
    #printing avg_pl rounded to 2 decimal places
    print(f"Average Change: ${round(avg_pl,2)}")
    txt_file.write(f'\nAverage Change: ${round(avg_pl,2)}')
    
    #using the _index values defined above to point to the row under the total_months list and combining that with the actual 
    #greatest increse/decrease value
    print(f"Greatest Increase in Profits: {Total_months[max_month_index+1]} (${greatest_increase})")
    txt_file.write(f'\nGreatest Increase in Profits: {Total_months[max_month_index+1]} (${greatest_increase})')
    print(f"Greatest Decrease in Profits: {Total_months[min_month_index+1]} (${greatest_decrease})")
    txt_file.write(f'\nGreatest Decrease in Profits: {Total_months[min_month_index+1]} (${greatest_decrease})')
