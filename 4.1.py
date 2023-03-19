class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]

class PhitronCompany:
    total_bus = 5
    total_bus_list = []
    def install(self):
        bus_no = int(input("Enter Bus no: "))
        flag = 0
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                print("Bus already installed")
                flag = 1
                break
        if flag == 0:
            bus_driver = input("Enter Bus Driver Name: ")
            bus_arrival = input("Enter Bus Arrival Time: ")
            bus_departure = input("Enter Bus Start Time: ")
            bus_from = input("Enter Bus Start From: ")
            bus_to = input("Enter Bus Destination To: ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\nBus installed successfully")

class BusCounter(PhitronCompany):
    user_lst = []
    bus_seat = 20
    def reservation(self):
        bus_no = int(input("Enter Bus Number: "))
        flag = 1
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                passenger = input("Enter Your Name: ")
                seat_no = int(input("Enter Your Seat Number: "))
                if seat_no - 1 > self.bus_seat:
                    print("Only 20 seats are available")
                elif bus['seat'][seat_no-1] != "Empty":
                    print("Seat already booked")
                else:
                     bus['seat'][seat_no - 1] = passenger
            else:
                flag = 0
                break
        if flag == 0:
            print("No bus Number Available")

    def showBusInfo(self):
        bus_no = int(input("Enter Bus No: "))
        for bus in self.total_bus_list:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"BUS NUMBER: {bus_no} \t\tDriver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\tDeparture: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\tTo: {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end=("\t"))
                        a+=1
                    print('\t', end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a+=1
                    print()
    def get_users(self):
        return self.user_lst
    def create_account(self):
        name = input("Enter your name: ")
        flag = 0
        for user in self.get_users():
            if user.username == name:
                print("Username already exists")
                flag = 1
                break
        if flag == 0:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account created successfully")

    def available_buses(self):
        if len(self.total_bus_list) == 0:
            print("No Bus Available")
        else:
            for bus in self.total_bus_list:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO{bus['coach']} {'#'*10}")
                print(f"BUS NUMBER: {bus['coach']} \t\tDriver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\tDeparture: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\tTo: {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end=("\t"))
                        a+=1
                    print('\t', end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a+=1
                    print()


while True:
    counter = BusCounter()
    print("1. Create an account \n2. Login To your account \n3. EXIT")
    user_input = int(input("Enter Your choice: "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        isAdmin = False
        flag = 0
        if name == 'admin' and password == '123':
            isAdmin = True
        if isAdmin == False:
            for user in counter.get_users():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"1. Available Buses \n2. Show bus info \n3. Reservation \n4. EXIT")
                    a = int(input("Enter your choice: "))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.available_buses()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.reservation()
            else:
                print("Please sign up")
        else:
            while True:
                print("Hello Admin, Welcome back!")
                print(f"1. Install Bus \n2. Available Buses \n3. Show Bus \n4. Show user list \n5. Exit")
                a = int(input("Enter your choice: "))
                if a == 5:
                    break
                elif a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_buses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    counter.get_users()

# company = PhitronCompany()
# company.install()

# b = BusCounter()
# b.reservation()
# b.showBusInfo()
