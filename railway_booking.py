# ==========================================
#       RAILWAY TICKET BOOKING SYSTEM
#             PYTHON MINI PROJECT
# ==========================================

# Train details stored as tuples inside a list
# (Train Number, Name, Source, Destination, Fare)

trains = [
    (101, "Rajdhani Express", "Delhi", "Mumbai", 1500),
    (102, "Shatabdi Express", "Delhi", "Agra", 500),
    (103, "Vande Bharat", "Delhi", "Varanasi", 1200),
    (104, "Duronto Express", "Mumbai", "Delhi", 1300),
    (105, "Garib Rath", "Delhi", "Jaipur", 700)
]

# Available seats for each train
available_seats = [100, 80, 100, 90, 70]

# List to store all bookings
bookings = []

# Booking ID counter
next_booking_id = [1001]


# ==========================================
# 1. DISPLAY AVAILABLE TRAINS
# ==========================================

def display_trains():

    print("\n========== AVAILABLE TRAINS ==========")

    for i in range(len(trains)):

        print("\nTrain Number:", trains[i][0])
        print("Train Name:", trains[i][1])
        print("Source:", trains[i][2])
        print("Destination:", trains[i][3])
        print("Fare: Rs.", trains[i][4])
        print("Available Seats:", available_seats[i])


# ==========================================
# 2. SEARCH TRAINS
# ==========================================

def search_train():

    source = input("\nEnter source station: ").strip().lower()
    destination = input("Enter destination station: ").strip().lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for i in range(len(trains)):

        if (trains[i][2].lower() == source and
            trains[i][3].lower() == destination):

            print("\nTrain Number:", trains[i][0])
            print("Train Name:", trains[i][1])
            print("Fare: Rs.", trains[i][4])
            print("Available Seats:", available_seats[i])

            found = True

    if found == False:
        print("Sorry! No trains found for this route.")


# ==========================================
# 3. BOOK TICKETS FOR MULTIPLE PASSENGERS
# ==========================================

def book_ticket():

    display_trains()

    train_number = int(input("\nEnter train number: "))

    train_index = -1

    for i in range(len(trains)):

        if trains[i][0] == train_number:
            train_index = i
            break

    if train_index == -1:
        print("Invalid train number!")
        return

    number_of_passengers = int(
        input("Enter number of passengers: ")
    )

    if number_of_passengers <= 0:
        print("Invalid passenger count!")
        return

    if number_of_passengers > available_seats[train_index]:
        print("Sorry! Not enough seats available.")
        return

    # List to store passenger details
    passengers = []

    for i in range(number_of_passengers):

        print("\nEnter details of Passenger", i + 1)

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))

        if name == "" or age <= 0:
            print("Invalid passenger details!")
            return

        passenger = (name, age)

        passengers.append(passenger)

    # Calculate total fare
    total_fare = (
        trains[train_index][4] * number_of_passengers
    )

    # Generate booking ID
    booking_id = next_booking_id[0]

    # Store complete booking
    booking = (
        booking_id,
        trains[train_index][1],
        trains[train_index][2],
        trains[train_index][3],
        passengers,
        number_of_passengers,
        total_fare
    )

    bookings.append(booking)

    # Update available seats
    available_seats[train_index] -= number_of_passengers

    next_booking_id[0] += 1

    # Display booking confirmation
    print("\n========== BOOKING CONFIRMED ==========")

    print("Booking ID:", booking_id)
    print("Train:", trains[train_index][1])
    print("Route:", trains[train_index][2], "to",
          trains[train_index][3])

    print("\nPassenger Details:")

    for passenger in passengers:

        print("Name:", passenger[0])
        print("Age:", passenger[1])

    print("\nTotal Passengers:", number_of_passengers)
    print("Total Fare: Rs.", total_fare)

    print("Remaining Seats:", available_seats[train_index])


# ==========================================
# 4. VIEW ALL BOOKINGS
# ==========================================

def view_bookings():

    print("\n========== ALL BOOKINGS ==========")

    if len(bookings) == 0:

        print("No bookings available.")

    else:

        for booking in bookings:

            print("\nBooking ID:", booking[0])
            print("Train:", booking[1])
            print("Route:", booking[2], "to", booking[3])

            print("\nPassenger Details:")

            for passenger in booking[4]:

                print("Name:", passenger[0])
                print("Age:", passenger[1])

            print("Total Passengers:", booking[5])
            print("Total Fare: Rs.", booking[6])


# ==========================================
# 5. CANCEL BOOKING
# ==========================================

def cancel_booking():

    booking_id = int(input("\nEnter Booking ID to cancel: "))

    found = False

    for i in range(len(bookings)):

        if bookings[i][0] == booking_id:

            # Find the train corresponding to booking
            for j in range(len(trains)):

                if (trains[j][1] == bookings[i][1] and
                    trains[j][2] == bookings[i][2] and
                    trains[j][3] == bookings[i][3]):

                    # Restore cancelled seats
                    available_seats[j] += bookings[i][5]
                    break

            bookings.remove(bookings[i])

            print("Booking cancelled successfully!")
            found = True
            break

    if found == False:

        print("Invalid Booking ID!")


# ==========================================
# 6. MAIN MENU
# ==========================================

while True:

    print("\n========================================")
    print("       RAILWAY TICKET BOOKING SYSTEM")
    print("========================================")

    print("1. Display Available Trains")
    print("2. Search Trains")
    print("3. Book Tickets")
    print("4. View All Bookings")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        display_trains()

    elif choice == "2":

        search_train()

    elif choice == "3":

        book_ticket()

    elif choice == "4":

        view_bookings()

    elif choice == "5":

        cancel_booking()

    elif choice == "6":

        print("\nThank you for using Railway Ticket Booking System!")
        print("Have a safe journey!")
        break

    else:

        print("Invalid choice! Please select again.")