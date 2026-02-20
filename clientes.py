#List for storing client data
clients = []


def add_client(name):
    """Registers a new client"""
    clients.append(name)
    print(f"Client {name} added successfully!")


def list_clients():
    """Displays a list of all registered clients"""
    print("\n--- Hotel Client List ---")
    if not clients:
        print("The list is empty.")
    else:
        for client in clients:
            print(f"- {client}")


def find_client(name):
    """Search client"""
    if name in clientes:
        print(f"Client {name} found in the system.")
        return True
    else:
        print(f"Client {name} not found.")
        return False
    

def delete_customer(name):
    """Delete client from list"""
    if name in clientes:
        clientes.remove(name)
        print(f"Client {name} has been removed.")
    else:
        print(f"Error: Client {name} not found.")