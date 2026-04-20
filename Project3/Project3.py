FIRST_CLASS_FEE = 50
taken_seats = []

while True:
    seat = int(input("Choose a seat from 1 to 20: "))

    if seat < 1 or seat > 20:
        print("Invalid seat number.")
        continue

    if seat in taken_seats:
        print("That seat is already taken.")
        continue

    if seat >= 9 and seat <= 16:
        answer = input("This is an emergency row seat. Can you help in an emergency? (yes/no): ")
        if answer.lower() != "yes":
            print("You cannot choose this seat.")
            continue

    taken_seats.append(seat)

    if seat >= 1 and seat <= 4:
        print("First class seat selected. Fee is $50.")
    else:
        print("Regular seat selected. No fee.")

    again = input("Do you want to buy another seat? (yes/no): ")
    if again.lower() != "yes":
        break

print("Seats purchased:", taken_seats)