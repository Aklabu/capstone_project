class Bus:
    def __init__(self, bus_id, driver_name, route, seats):
        self.bus_id = bus_id
        self.driver_name = driver_name
        self.route = route
        self.seats = seats
        self.passenger_list = []

    def display_info(self):
        print(f"Bus ID: {self.bus_id}")
        print(f"Driver Name: {self.driver_name}")
        print(f"Route: {self.route}")
        print(f"Available Seats: {self.seats - len(self.passenger_list)}\n")

    def book_seat(self, passenger_name):
        if len(self.passenger_list) < self.seats:
            self.passenger_list.append(passenger_name)
            print(f"Seat booked successfully for {passenger_name}!")
        else:
            print("Sorry, no available seats!")

    def display_passengers(self):
        if self.passenger_list:
            print("Passenger List:")
            for i, passenger in enumerate(self.passenger_list, start=1):
                print(f"{i}. {passenger}")
        else:
            print("No passengers yet.")

def main_menu():
    print("\n=== Bus Management System ===")
    print("1. View Bus Information")
    print("2. Book a Seat")
    print("3. View Passenger List")
    print("4. Exit")

def main():
    # Create a bus instance
    bus = Bus(bus_id="B001", driver_name="John Doe", route="City Center - Airport", seats=5)

    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            bus.display_info()
        elif choice == "2":
            passenger_name = input("Enter passenger name: ")
            bus.book_seat(passenger_name)
        elif choice == "3":
            bus.display_passengers()
        elif choice == "4":
            print("Exiting Bus Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
