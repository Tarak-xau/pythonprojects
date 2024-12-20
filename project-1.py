class Hotel:
    def __init__(self, num_rooms):
        self.rooms = ["Available" for _ in range(num_rooms)]

    def display_status(self):
        print(f"\nAvailable Rooms: {self.rooms.count('Available')}")
        print(f"Booked Rooms: {self.rooms.count('Booked')}\n")

    def check_availability(self):
        print("\nRoom Status:")
        print("\n".join([f"Room {i + 1}: {status}" for i, status in enumerate(self.rooms)]))

    def book_room(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            if self.rooms[room_number - 1] == "Available":
                self.rooms[room_number - 1] = "Booked"
                print(f"Room {room_number} has been successfully booked.")
            else:
                print(f"Room {room_number} is already booked.")
        else:
            print("Invalid room number. Please try again.")

    def cancel_booking(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            if self.rooms[room_number - 1] == "Booked":
                self.rooms[room_number - 1] = "Available"
                print(f"Booking for Room {room_number} has been successfully canceled.")
            else:
                print(f"Room {room_number} is not booked.")
        else:
            print("Invalid room number. Please try again.")


def main():
    print("Welcome to the Hotel Booking System!")
    while True:
        num_rooms = input("Enter the number of rooms in the hotel: ")
        if num_rooms.isdigit() and int(num_rooms) > 0:
            num_rooms = int(num_rooms)
            break
        else:
            print("Please enter a valid positive number.")

    hotel = Hotel(num_rooms)

    while True:
        print("\nMenu:")
        print("1. Check room availability")
        print("2. Book a room")
        print("3. Cancel a booking")
        print("4. Display summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            hotel.check_availability()
        elif choice == "2":
            room_number = input("Enter room number to book: ")
            if room_number.isdigit():
                hotel.book_room(int(room_number))
            else:
                print("Invalid input. Please enter a valid room number.")
        elif choice == "3":
            room_number = input("Enter room number to cancel booking: ")
            if room_number.isdigit():
                hotel.cancel_booking(int(room_number))
            else:
                print("Invalid input. Please enter a valid room number.")
        elif choice == "4":
            hotel.display_status()
        elif choice == "5":
            print("Thank you for using the Hotel Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()