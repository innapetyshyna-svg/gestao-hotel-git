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