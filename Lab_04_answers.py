Groceries = ['bananas','strawberries','apples','bread']
Groceries.append('champaign')
print Groceries
Groceries.remove('bread')
item_search = raw_input("Enter the name of what you want : ")
aisle_dict = {
    'apples':'a',
    'bananas':'b',
    'bread':'b',
    'champaigne':'c',
    'strawberries':'s'
    }
print "You can find",item_search,"in aisle",aisle_dict[item_search]
print "************************************"
print "************************************"
items_search = raw_input("Enter the name of the fruit whose price you want to find : ")
print "************************************"
print "************************************"

##b
item_prices= {
    'apples':'SPIC_APLES',
    'Bananas':'SPIC_BANANAS',
    'Bread':'SPIC_BREAD',
    'Carrots':'SPIC_CARROTS',
    'Champaigne':'SPIC_CHAMPAIGN',
    'Strawberries':'SPIC_STRAWBERRIES'
    }
print item_prices[items_search]
print "************************************"
print "************************************"

### C ##changing the price of stawberry
item_prices['Strawberries']='WPIC_STRAWBERRIES'
print "The price of strawberries has changed to",item_prices['Strawberries']
## d##
item_prices['chicken'] = 'SPIC_CHICKEN'
print "New items in stock"
for i in item_prices:
    print i
print "************************************"
print "************************************"

####################################3
#####################33
## Q3b
always_in_stock = ('apples','Bananas','Bread','Carrots','Champaigne','Strawberries')
print "************************************"
print "These are always available"
for j in always_in_stock:  
    print j'''
print "************************************"
print "************************************"
################################
################################
###

