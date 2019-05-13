
'''
Version 1
'''
#You have two loops, it's a common intuition that a second inner loop 
#can be replaced with a data structure

#Which structure do we choose? One that enforces our constraints.
#int(data[row][0]) == id #here you check for uniqueness
#So a set or a dictionary can be a good choice

orders = {} #Replace your inner loop with a dictionary
order_averages = {}

for row in data: #This is also a dictionary
    row_id = int(row[0])
    
    #We don't have to set variables ahead of time because Python gives for free
    #in a dynamic way
    #To be fair, we lost labels, which would be fixed by using a named tuple
    
    row_values = orders.setdefault(row_id, (0, 0.0)) #immutable length
    tot = row_values[1] + float(row[4].strip(" ").strip("$"))
    qty = row_values[0] + int(row[1])
    avg = tot / qty
    orders[row_id] = (qty, tot)
    
    order_averages[row_id] = float(format(avg, ".2f")) 

ord_avg = tuple(order_averages.items())  
print ord_avg[1830:1835]

'''
Version 2
'''

#separate summing and averaging
orders = {}
for row in data: 
    row_id = int(row[0])
    
    row_values = orders.setdefault(row_id, (0, 0.0)) #immutable length
    tot = row_values[1] + float(row[4].strip(" ").strip("$"))
    qty = row_values[0] + int(row[1])
    orders[row_id] = (qty, tot)

order_averages = {}    
for item_id, values in orders.items():
    avg = values[1] / values[0]
    order_averages[item_id] = float(format(avg, ".2f")) 

ord_avg = tuple(order_averages.items())  
print ord_avg[1830:1835]


'''
Version 3
'''
#Separate collection and averaging
orders = {}
for row in data: 
    row_id = int(row[0])
    #mutable length since we are collecting
    order = orders.setdefault(row_id, {'quantities': [], 'prices': []})
    order['prices'] += [float(row[4].strip(" ").strip("$"))]
    order['quantities'] += [int(row[1])]
    orders[row_id] = order

order_averages = {}
for order_id, values in orders.items():
    avg = sum(values['prices']) / sum(values['quantities'])
    order_averages[order_id] = float(format(avg, ".2f"))  

ord_avg = tuple(order_averages.items())  
print ord_avg[1830:1835]
