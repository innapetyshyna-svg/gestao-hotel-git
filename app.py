from clientes import add_client, list_clients, find_client, delete_customer, clients
from quartos import get_all_rooms, book_room, check_out_room, get_available_rooms, rooms_db
from reservas import create_reservation, cancel_reservation, check_reservation, reservations


add_client("Ana")


list_clients()


book_room_1 = book_room(205)

clients_1 = clients[0]

create_reservation(205, clients_1, rooms_db)
