log_file = open("um-server-01.txt") # opens server so we have access to the info inside of it


def sales_reports(log_file): # creating a variable for the sales reports
    for line in log_file: # looping through the all the reports
        line = line.rstrip() # 
        day = line[0:3] # grabbing a specific line of a day 
        if day == "Mon":
            print(line) # if the day we grabbed is equal to mon/tue we will print out that line


sales_reports(log_file)
