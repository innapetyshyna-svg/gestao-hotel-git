## Database of rooms (Room number: Status)
# True means Available, False means Occupied
rooms_db = {
    101: True,
    102: True,
    103: True,
    201: True,
    202: True,
    203: True,
    204: True,
    205: True
}


def get_all_rooms():
    """Returns the list of all rooms and their status"""
    return rooms_db


def book_room(room_number):
    """Sets the room status to Occupied (False)"""
    if room_number in rooms_db:
        rooms_db[room_number] = False
        print(f"Room {room_number} has been booked.")
    else:
        print("Room not found.")