# Shipping manager module for handling shipping operations using dictionaries, sets and lists.

# Declaration of the shipment dictionary and region sets
shipment = {}
cities = set()
north_region = set()
south_region = set()
east_region = set()
west_region = set()
middle_region = set()


# Definition of functions for managing shipments

def add_shipment(shipping_id, destination, region, status):
    cities.add(destination)
    if region == "NORTH":
        north_region.add(destination)
    elif region == "SOUTH":
        south_region.add(destination)
    elif region == "EAST":
        east_region.add(destination)
    elif region == "WEST":
        west_region.add(destination)
    elif region == "MIDDLE":
        middle_region.add(destination)
    if shipping_id not in shipment:
        shipment[shipping_id] = {
            "destination": destination,
            "region": region,
            "status": status
        }
        print(f"Shipment '{shipping_id}' added.")
        return True
    else:
        print(f"Shipment '{shipping_id}' already exists.")
        return False


def update_shipment_status(shipping_id, new_status):
    if shipping_id in shipment:
        shipment[shipping_id]["status"] = new_status
        print(f"Shipment '{shipping_id}' status updated to '{new_status}'.")
        return True
    else:
        print(f"Shipment '{shipping_id}' does not exist.")
        return False


def remove_shipment(shipping_id):
    if shipping_id in shipment:
        destination = shipment[shipping_id]["destination"]
        region = shipment[shipping_id]["region"]
        del shipment[shipping_id]
        if destination not in [details["destination"] for details in shipment.values()]:
            cities.remove(destination)
        if region == "NORTH":
            if destination not in [details["destination"] for details in shipment.values() if details["region"] == "NORTH"]:
                north_region.remove(destination)
        elif region == "SOUTH":
            if destination not in [details["destination"] for details in shipment.values() if details["region"] == "SOUTH"]:
                south_region.remove(destination)
        elif region == "EAST":
            if destination not in [details["destination"] for details in shipment.values() if details["region"] == "EAST"]:
                east_region.remove(destination)
        elif region == "WEST":
            if destination not in [details["destination"] for details in shipment.values() if details["region"] == "WEST"]:
                west_region.remove(destination)
        elif region == "MIDDLE":
            if destination not in [details["destination"] for details in shipment.values() if details["region"] == "MIDDLE"]:
                middle_region.remove(destination)
        print(f"Shipment '{shipping_id}' removed.")
        return True
    else:
        print(f"Shipment '{shipping_id}' does not exist.")
        return False


# Definition of functions for filtering and displaying shipments

def shipment_by_id(shipping_id):
    if shipping_id in shipment:
        details = shipment[shipping_id]
        print(f"Shipment ID: {shipping_id}")
        print(f" - Destination: {details['destination']}")
        print(f" - Region: {details['region']}")
        print(f" - Status: {details['status']}")
    else:
        print(f"Shipment '{shipping_id}' does not exist.")

def shipment_by_status(status):
    filtered_shipments = {sid: details for sid, details in shipment.items() if details["status"] == status}
    if filtered_shipments:
        print(f"Shipments with status '{status}':")
        for sid, details in filtered_shipments.items():
            print(f" - ID: {sid}, Destination: {details['destination']}")
    else:
        print(f"No shipments found with status '{status}'.")


def shipment_by_destination(destination):
    filtered_shipments = {sid: details for sid, details in shipment.items() if details["destination"] == destination}
    if filtered_shipments:
        print(f"Shipments to destination '{destination}':")
        for sid, details in filtered_shipments.items():
            print(f" - ID: {sid}, Status: {details['status']}")
    else:
        print(f"No shipments found to destination '{destination}'.")


def shipment_by_region(region):
    filtered_shipments = {sid: details for sid, details in shipment.items() if details["region"] == region}
    if filtered_shipments:
        print(f"Shipments in region '{region}':")
        for sid, details in filtered_shipments.items():
            print(f" - ID: {sid}, Destination: {details['destination']}, Status: {details['status']}")
    else:
        print(f"No shipments found in region '{region}'.")


def show_shipments_keys():
    if shipment:
        print("Shipment IDs:")
        for sid in shipment.keys():
            print(f" - {sid}")
    else:
        print("No shipments available.")


def show_shipments_values():
    if shipment:
        print("Shipment Details:")
        for details in shipment.values():
            print(f" - Destination: {details['destination']}, Region: {details['region']}, Status: {details['status']}")
    else:
        print("No shipments available.")


def show_shipments_items():
    if shipment:
        print("Shipment Items:")
        for sid, details in shipment.items():
            print(f" - ID: {sid}, Destination: {details['destination']}, Region: {details['region']}, Status: {details['status']}")
    else:
        print("No shipments available.")


def show_all_cities():
    if cities:
        print("Cities with shipments:")
        for city in cities:
            print(f" - {city}")
    else:
        print("No cities available.")


def show_region_summary():
    print("Region Summary:")
    print(f" - North Region: {len(north_region)} cities")
    print(f" - South Region: {len(south_region)} cities")
    print(f" - East Region: {len(east_region)} cities")
    print(f" - West Region: {len(west_region)} cities")
    print(f" - Middle Region: {len(middle_region)} cities")


def show_all_shipments():
    if shipment:
        print("All Shipments:")
        for sid, details in shipment.items():
            print(f" - ID: {sid}, Destination: {details['destination']}, Region: {details['region']}, Status: {details['status']}")
    else:
        print("No shipments available.")

# Loading initial shipments for testing purposes
add_shipment("SHP1001", "MIAMI", "NORTH", "IN TRANSIT")
add_shipment("SHP1002", "DALLAS", "SOUTH", "PENDING")
add_shipment("SHP1003", "ATLANTA", "EAST", "DELIVERED")
add_shipment("SHP1004", "SEATTLE", "WEST", "SHIPPED")
add_shipment("SHP1005", "CHICAGO", "MIDDLE", "IN TRANSIT")
add_shipment("SHP1006", "MIAMI", "NORTH", "DELIVERED")
add_shipment("SHP1007", "DALLAS", "SOUTH", "IN TRANSIT")
add_shipment("SHP1008", "BOSTON", "EAST", "PENDING")
add_shipment("SHP1009", "LOS ANGELES", "WEST", "DELIVERED")
add_shipment("SHP1010", "DENVER", "MIDDLE", "SHIPPED")


def show_menus():
    print("Shipping Manager Menu:")
    while True:
        print("1. Add Shipment")
        print("2. Update Shipment Status")
        print("3. Remove Shipment")
        print("4. Show Shipments by ID")
        print("5. Show Shipments by Status")
        print("6. Show Shipments by Destination")
        print("7. Show Shipments by Region")
        print("8. Show Shipment IDs")
        print("9. Show Shipment Details")
        print("10. Show Shipment Items")
        print("11. Show All Cities")
        print("12. Show Region Summary")
        print("13. Show All Shipments")
        print("14. Exit")
        print("\n" + "-"*80)
        choice = input("Enter your choice: ")

        if choice == "1":
            shipping_id = input("Enter shipment ID: ").upper()
            destination = input("Enter destination city: ").upper()
            region = input("Enter region (North/South/East/West/Middle): ").upper()
            if region not in ["NORTH", "SOUTH", "EAST", "WEST", "MIDDLE"]:
                print("Invalid region. Please enter a valid region.")
                continue
            status = input("Enter shipment status: ").upper()
            if status not in ["PENDING", "SHIPPED", "DELIVERED", "IN TRANSIT"]:
                print("Invalid status. Please enter a valid status.")
                continue
            add_shipment(shipping_id, destination, region, status)
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "2":
            shipping_id = input("Enter shipment ID to update: ").upper()
            new_status = input("Enter new status: ").upper()
            if new_status not in ["PENDING", "SHIPPED", "DELIVERED", "IN TRANSIT"]:
                print("Invalid status. Please enter a valid status.")
                continue
            update_shipment_status(shipping_id, new_status)
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "3":
            shipping_id = input("Enter shipment ID to remove: ").upper()
            remove_shipment(shipping_id)
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "4":
            shipping_id = input("Enter shipment ID to display: ").upper()
            shipment_by_id(shipping_id)
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "5":
            status = input("Enter status to filter by: ").upper()
            if status not in ["PENDING", "SHIPPED", "DELIVERED", "IN TRANSIT"]:
                print("Invalid status. Please enter a valid status.")
                continue
            shipment_by_status(status)
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "6":
            destination = input("Enter destination to filter by: ").upper()
            shipment_by_destination(destination)
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "7":
            region = input("Enter region to filter by (North/South/East/West/Middle): ").upper()
            if region not in ["NORTH", "SOUTH", "EAST", "WEST", "MIDDLE"]:
                print("Invalid region. Please enter a valid region.")
                continue
            shipment_by_region(region)
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "8":
            show_shipments_keys()
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "9":
            show_shipments_values()
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "10":
            show_shipments_items()
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "11":
            show_all_cities()
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "12":
            show_region_summary()
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "13":
            show_all_shipments()
            input("\nPress Enter to continue...")
            print("\033[H\033[2J", end="")

        elif choice == "14":
            print("Exiting Shipping Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_menus()
