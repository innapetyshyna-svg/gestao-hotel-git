# List to store reservations: {"room": room_number, "client": client_name}
reservations = []


def create_reservation(room_number, client_name, rooms_db):
    """Checks if the room is free and creates a reservation"""
    if room_number in rooms_db and rooms_db[room_number] == True:
        rooms_db[room_number] = False  # Mark room as occupied
        reservations.append({"room": room_number, "client": client_name})
        print(f"Reservation confirmed: Room {room_number} for {client_name}.")
    else:
        print(f"Room {room_number} is not available or doesn't exist.")


def cancel_reservation(room_number, rooms_db):
    """Removes the reservation and makes the room available again"""
    global reservations
    # Find the reservation
    initial_count = len(reservations)
    reservations = [res for res in reservations if res["room"] != room_number]
    
    if len(reservations) < initial_count:
        rooms_db[room_number] = True  # Mark room as available
        print(f"Reservation for room {room_number} has been canceled.")
    else:
        print(f"No reservation found for room {room_number}.")