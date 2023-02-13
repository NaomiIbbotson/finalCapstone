
#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        '''Initialises shoe object'''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
      
    def get_cost(self):
        '''Returns the cost of the shoe as a float'''
        return float(self.cost)
        

    def get_quantity(self):
        '''Returns the quantity of the shoes as an int'''
        return int(self.quantity)
        
    def __str__(self):
        '''Returns a string representation of the class.'''
        return f"""
Country: {self.country}
Code: {self.code}
Product: {self.product}
Cost: {self.cost}
Quantity: {self.quantity}"""


#==========Functions outside the class==============
def read_shoes_data():
    '''
    Declares an empty shoes list.
    Opens the file inventory.txt and reads the data from this file.
    Creates a shoes object from each line of data and
    appends this object into the shoes list.
    '''
    shoe_list = []
    try:
        with open("inventory.txt", "r") as f:
            next(f)
            for line in f:
                stripped_line = line.strip("\n")
                list_line = stripped_line.split(",")
                shoes = Shoe(list_line[0], list_line[1], list_line[2], list_line[3], list_line[4])
                shoe_list.append(shoes)
    except FileNotFoundError:
        print("File does not exist")

    return shoe_list


def capture_shoes(shoe_list):
    '''
    Allows a user to capture data
    about a shoe and uses this data to create a shoe object
    and appends this object inside the shoe list.
    Then updates the inventory file.
    '''
    # Get shoe data from user.
    country = input("Enter the country: ")
    code = input("Enter the product code: ")
    product = input("Enter the product name:")
    # Checking cost an quantity are numbers
    while True:
        cost = input("Enter the cost: ")
        try:
            check_is_num = float(cost)
            break
        except:
            print("Please enter a number.")

    while True:
        quantity = input("Enter the quantity: ")
        try:
            check_is_num = int(quantity)
            break
        except:
            print("Please enter a whole number.")

    # reating shoe object
    shoe = Shoe(country, code, product, cost, quantity)

    # Ading to shoe list
    shoe_list.append(shoe)

    # Adding to file
    with open("inventory.txt", "a") as f:
        f.write(f"{country},{code},{product},{cost},{quantity}\n")
    

def view_all(shoe_list):
    '''
    Iterates over the shoes list and prints the details of the shoes
    returned from the __str__ function.
    '''
    for shoe in shoe_list:
        print(shoe.__str__())
    

def re_stock(shoe_list):
    '''
    Finds the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Asks the user if they
    want to add to this quantity of shoes and then updates it in the shoe list and file
    '''
    # Finding lowest stock quantity index num
    lowest = shoe_list[0].get_quantity()
    index_num = 0
    for num, shoe in enumerate(shoe_list):
        if shoe.get_quantity() < lowest:
            lowest = shoe.get_quantity()
            index_num = num

    # Displaying the shoe with the lowest stock getting restock quantity from user
    print(shoe_list[index_num])
    choices = ["y", "n"]
    choice = ""
    while choice not in choices:
        choice = input("Would you like to restock this item? y/n: ").lower()
        if choice not in choices:
            print("please enter a valid choice.")

    if choice == "n":
        return
    else:
        quantity = 0
        while True:
            quantity = input("Enter the quantity:")
            try:
                quantity = int(quantity)
                if quantity < 0:
                    print("Please enter a positive number")
                else:
                    break
            except:
                print("You did not enter a valid number")

    # Adding the amount to restock
    total = shoe_list[index_num].get_quantity() + quantity
    shoe_list[index_num].quantity = str(total)

    # Writing to file
    with open("inventory.txt", "w") as f:
        f.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            
    return shoe_list
    

def search_shoe(shoe_list):
    '''
     Searches for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # List of SKU numbers
    codes = []
    for shoe in shoe_list:
        codes.append(shoe.code)

    # Get code from user and check it exists
    input_code = ""
    while input_code not in codes:
        input_code = input("Please enter the code of the shoe you would like to search for: ")
        if input_code not in codes:
            print("This code does not exist, please try again.")

    # Get index num for code and return shoe at that index
    index = codes.index(input_code)
    return shoe_list[index]

    

def value_per_item(shoe_list):
    '''
    Calculates the total value for each item.
    Value = cost * quantity.
    Prints this information on the console for all the shoes.
    '''
    total = 0
    for shoe in shoe_list:
        cost = shoe.get_cost()
        quantity = shoe.get_quantity()
        value = cost * quantity
        total += value
        print(f"Product: {shoe.product}\nValue:{value}\n")
    
    print(f"Total stock value: {total}\n")


def highest_qty(shoe_list):
    '''
    Determines the product with the highest quantity and
    prints this shoe as being for sale.
    '''
        # Finding lowest stock quantity index num
    highest = int(shoe_list[0].quantity)
    index_num = 0
    for num, shoe in enumerate(shoe_list):
        if int(shoe.quantity) > highest:
            highest = int(shoe.quantity)
            index_num = num

    # Printing the shoe with highest stock is for sale
    print(f"{shoe_list[index_num].product} is for sale.")



shoe_list = read_shoes_data()
'''The list will be used to store a list of objects of shoes.'''

#==========Main Menu=============

while True:
    #presenting the menu to the user and 
    # making sure that the input is converted to lower case.
    menu = input("""Select one of the following Options below:
va - View all stock items
a - Add a stock item
r - restock lowest stocked item
s - search for an item by code
v - view the value of all stock items
fs - view item for sale
e - Exit
: """).lower()

    # Displaying all stock items
    if menu == "va":
      view_all(shoe_list)

    # Adding a stock item
    elif menu == "a":
        capture_shoes(shoe_list)
    
    # Restocking lowest stock item
    elif menu == "r":
       shoe_list = re_stock(shoe_list)

    # Search for a shoe by code
    elif menu == "s":
        print(search_shoe(shoe_list))

    # Dispalays the total value for each product and the total
    elif menu == "v":
        value_per_item(shoe_list)

    # Displays the shoe with the highest quantity as for sale
    elif menu == "fs":
        highest_qty(shoe_list)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")