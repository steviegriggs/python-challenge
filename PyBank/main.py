import os
import csv

csvpath = os.path.join('budget_data.csv')

def avg(list):
    tot=0
    for numb in list:
        tot = tot + numb
    return tot / len(list)



with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)

    #making individual lists of months and  their respective profit/loss
        # months = list of months
        # pl = list of Profit/loss in floating point form
    months = []
    pl = [] 
    for x in csvreader:
        months.append(x[0])
        pl.append(int(x[1]))

    #m_count = total number of months
    m_count = len(months)    
    
    #net_pl = net total amount of "Profit/Losses" over the entire period
    net_pl = 0
    for x in pl:
        net_pl = net_pl + x

    
    #delta is a list of the difference in the PL of month and previous month
        # indexing in delta is one less than indexing in pl and months
    delta = []
    y=0
    while y < len(pl)-1:
        delta.append(pl[y+1]-pl[y])
        y=y+1 
    
    #delta_avg = average of all the values in the list delta
    delta_avg = avg(delta)
    
    #gr_inc will be the value of the greatest increase
    #gr_dec will be the value of the greatest decrease
        #will pull the corresponding dates through indexes
    gr_inc = 0
    gr_dec = 0
    for x in delta:
        if x > gr_inc:
            gr_inc = x
            increase_index = delta.index(x)
        elif x < gr_dec:
            gr_dec = x
            decrease_index = delta.index(x)

    inc_date = months[increase_index+1]
    dec_date = months[decrease_index + 1]

    #rd_avg is a nicer formatted (2 decimal digits) version of the average change
    rd_avg= round(delta_avg,2)

    b_print = []
    b_print.append("Financial Analysis")
    b_print.append("----------------------------")
    b_print.append(f"Total Months: {m_count}")
    b_print.append(f"Total: ${net_pl}")
    b_print.append(f"Average Change: ${rd_avg}")
    b_print.append(f"Greatest Increase in Profits: {inc_date} (${gr_inc})")
    b_print.append(f"Greatest Decrease in Profits: {dec_date} (${gr_dec})")

    bank_txt= open("financial_analysis.txt","w+")
    for x in b_print:
        print(x)
        print(x, file = bank_txt)
    bank_txt.close
    