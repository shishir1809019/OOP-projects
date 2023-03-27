class User:
    user_list = []
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Item:
    def __init__(self, itemId, price, description, quantity):
        self.itemID = itemId
        self.price = price
        self.description = description
        self.quantity = quantity
class ShoppingBasket:
    user_list = []
    user_ordered_data = {}
    itemsDB = []

    def get_users_list(self):
        return self.user_list
    
    def create_account(self):
        name = input("Enter your name: ")
        isNameExist = False
        
        for user in self.get_users_list():
            if user.username == name:
                print("User Already exist")
                break
        if isNameExist==False:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_list.append(vars(self.new_user))
            print("Account created successfully")

    def addItemToCard(self, username):
        itemid = input("Enter Item id: ")
        quantity = int(input("Enter item quantity: "))
        flag = 0
        price = 0
        for i in self.itemsDB:
            if i['itemID'] == itemid and i['quantity'] >= quantity:
                price = i['price']
                print("Item available")
                flag = 1
                break
        if not flag:
            print("Item not available")
        else:
            if self.user_ordered_data.get(username) == None:
                self.user_ordered_data[username] = []

            self.user_ordered_data[username] += [{'itemID': itemid, 'price': price, 'quantity': quantity }]

    def updateProductCart(self, username):
        itemid = input("Enter item id: ")
        quantity = int(input("Enter update quantity Number: "))
        for i in self.user_ordered_data[username]:
            if i.get('itemID') == itemid:
                if quantity <= i['quantity']:
                    i['quantity'] += quantity
                else: 
                    print("Out of stock")
                    break
    
    def deleteProductCart(self, username, itemid):
        flag = 0
        for i in self.itemsDB:
            if i['itemID'] == itemid:
                flag = 1
        if flag:
            for i in self.user_ordered_data[username]:
                if i['itemID'] == itemid:
                    self.user_ordered_data[username].remove(i)
                    print("Remove successfully")

    def showCart(self, username):
        print("Item ID\t Item price\t Item quantity")
        total_price = 0
        if  self.user_ordered_data.get(username) is not None:
            for i in self.user_ordered_data[username]:
                print(f"{i['itemID']}\t\t {i['price']}\t\t {i['quantity']}")
                total_price += i['price'] * i['quantity']
            print("_________________________________________________________")
            print(f"Total price = {total_price}")
        else:
            print("Empty Cart")

    
    def addItemToDatabase(self):
        itemid = input("Enter itemid: ")        
        isItemAvailable = False

        for  i in self.itemsDB:
            if i['itemID'] == itemid:
                isItemAvailable = True
                break
        if isItemAvailable == False:
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            self.new_item = Item(itemid, price, description, quantity)
            self.itemsDB.append(vars(self.new_item))
        else:
            print("Item already added")
    
    def delProductFromDatabase(self):
        itemid = input("Enter itemId: ")
        for i in self.itemsDB:
            if i['itemID'] == itemid:
                self.itemsDB.remove(i)
                print("Item removed successfully")
    def showItemsTable(self):
        print("Item ID \tItem Description \tItem Price \tItem quantity")
        for i in self.itemsDB:
            print(f"{i['itemID']}\t\t {i['description']}\t\t\t {i['price']}\t\t\t {i['quantity']}") 

basket = ShoppingBasket()
# basket.addItemToDatabase()
# basket.showData()


while True:
    print("1. Create an account\n2. Login to your account\n3. EXIT")
    user_choice = int(input("Enter your choice: "))
    if user_choice == 3:
        break
    elif user_choice == 1:
        basket.create_account()
    elif user_choice == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        isAdmin = False
        if name == 'admin' and password == '123':
            isAdmin = True
        if isAdmin == False:
            isNameExist = False
            for user in basket.user_list:
                if user['username'] == name and user['password'] == password:
                    isNameExist = True
                    break
            if isNameExist:
                while True:
                    print("1. Add item to your cart\n2. Update your cart\n3. Delete your cart\n4. Show your cart\n5. EXIT")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        basket.addItemToCard(name)
                    elif choice == 2:
                        basket.updateProductCart(name)
                    elif choice == 3:
                        itemid = input("Enter item id: ")
                        basket.deleteProductCart(name, itemid)
                    elif choice == 4:
                        basket.showCart(name)
                    else:
                        break
            else:
                print("User not exist!")
                break
        else:
            while True:
                print("HEllo admin!")
                print(f"1. Add new item \n2. Show new item \n3. Delete Item \n4. Exit")
                a = int(input("Enter your choice: "))
                if a == 5:
                    break
                elif a == 1:
                    basket.addItemToDatabase()
                elif a == 2:
                    basket.showItemsTable()
                elif a == 3:
                    basket.delProductFromDatabase()
                elif a == 4:
                    break



# b = ShoppingBasket()
# b.create_account()
# print(b.get_users_list())