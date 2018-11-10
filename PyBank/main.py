##Analyzing financial records


import csv
import os

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    file_header = next(csvreader)
    
#setting variables and creating 3 list 
    total_line_count = 0
    total_pl = 0
    indx_row_value=[]
    list_v=[]  
    date_list=[]
    
    for indx, row in enumerate(csvreader):    
        
#calculates total number of months in the data sheet

        total_line_count = total_line_count + 1
    
#Total net amount profit/losses for the entire period 

        total_pl += int(row[1])
    
#This creates a list: for every row, the profit/losses value will append to indx_row_value.  

        indx_row_value.append(int(row[1]))
    
#for every index value > 0 

        if indx > 0:
#subtracts the first value from the profit/losses column and subtracts the value from the indx_row_list [indx - 1] and sets the result to variable v,  

            v = int(row[1])-(int(indx_row_value[indx - 1]))
    
#takes the value (v) and appends it to a list named: list_v

            list_v.append(int(v))
    
#Takes the value of the frist row, first column (month/year) and appends to list named: date_list   
           date_list.append(row[0])   
            
#calculates average change by summing the the values in list_v and dividing by the lenght of list_v 

avg_change = int(sum(list_v)) / len(list_v)

#greatest increase in profits by finding the max number in list_v

greatest_pl_increase = int(max(list_v))

#greatest decrease in profits by finding the min number in list_v

greatest_pl_decrease = int(min(list_v))  

#finds the index number of the max value(greatest_pl_increase) to later refrence 
#the corresponding value in date_list refrenced in the print statement.

greatest_index = list_v.index(greatest_pl_increase)

#finds the index number of the min value (greatest_pl_decrease) to later refrence
#the corresponding value in date_list refrenced in the print statement.

least_index = list_v.index(greatest_pl_decrease)

print("Financial Analysis") 
print("---------------------------------------------")
print("Total Months: "+ str(total_line_count ))
print("Total: " + "$" + str(total_pl))                         
print("Total Average Change: " + "$" + str(avg_change))  
print("Greatest Increase in Profits: " + date_list[greatest_index] +" "+ str(greatest_pl_increase))
print("Greatest Decrease in Profits: " + date_list[least_index] + " " + str(greatest_pl_decrease))  

#writes the results to a txt file pybank_output.

results = open("pybank_output.txt","w")

results.write("Financial Analysis")
results.write("\n-------------------")
results.write("\nTotal Months: "+ str(total_line_count))
results.write("\nTotal: " + "$" + str(total_pl))                         
results.write("\nTotal Average Change: " + "$" + str(avg_change))  
results.write("\nGreatest Increase in Profits: " + date_list[greatest_index] +" "+ "(" + str(greatest_pl_increase) + ")")
results.write("\nGreatest Decrease in Profits: " + date_list[least_index] + " " + "( " + str(greatest_pl_decrease) + ")")  

results.close()

