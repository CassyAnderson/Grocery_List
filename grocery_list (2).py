

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

#Task: Create the empty data structure

grocery_history = []

#Variable used to check if the while loop condition is met
stop = 'go'

while stop != 'q' :
    grocery_item = {}
   
  #Accept input of the name of the grocery item purchased.
    item_name = input("Item name:\n")
    
    #Accept input of the quantity of the grocery item purchased.
    quantity = input("Quantity purchased:\n")
    
    #Accept input of the cost of the grocery item input (this is a per-item cost).
    cost = input("Price per item:\n")
    
    #Using the update function to create a dictionary entry which contains the name, number and price entered by the user.
    grocery_item['name'] = item_name
    grocery_item['number'] = int(quantity)
    grocery_item['price'] = float(cost) 
    
    #Add the grocery_item to the grocery_history list using the append function
    grocery_history.append(grocery_item)  
    
    #Accept input from the user asking if they have finished entering grocery items.
    stop = input("Would you like to enter another item?\n Type 'c' for continue or 'q' to quit:\n")   
    

# # Define variable to hold grand total called 'grand_total'
grand_total = 0

#Define a 'for' loop.  
for element in grocery_history:

  #Calculate the total cost for the grocery_item.
  item_total = element['number'] * element['price']
  
  #Add the item_total to the grand_total
  grand_total = item_total + grand_total
  
  #Output the information for the grocery item to match this example:
  #2 apple	@	$1.49	ea	$2.98
  print(str(element['number']) + " " + element['name'] + " @ $" + str(element['price']) + " ea $" + str(item_total))
  
  #Set the item_total equal to 0
item_total = 0

##Print the grand total
print("Grand total: " + "$" + str(grand_total))
