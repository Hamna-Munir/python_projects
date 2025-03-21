from prettytable import PrettyTable

#Create a table with headers
table = PrettyTable(["Student Name","Class","Subject","Marks"])

# Add rows for different subjects

table.add_row(["Ayra" , "7th" , "English" , "98"])
table.add_row(["Hina" , "7th" , "English" , "87"])
table.add_row(["Hira" , "7th" , "English" , "63"])
table.add_row(["Ashifa" , "7th" , "English" , "77"])    
table.add_row(["Mirha" , "7th" , "English" , "95"])     
print(table)     