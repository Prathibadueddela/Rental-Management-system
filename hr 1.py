class RentalProperty:
    def __init__(self, address, bedrooms, bathrooms, rent, available=True):
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.rent = rent
        self.available = available

class RentalManager:
    def __init__(self):
        self.properties = []

    def add_property(self, address, bedrooms, bathrooms, rent):
        property = RentalProperty(address, bedrooms, bathrooms, rent)
        self.properties.append(property)
        print("Property added successfully.")

    def view_properties(self):
        print("Rental Properties:")
        for i, property in enumerate(self.properties, 1):
            print(f"{i}. Address: {property.address}, Bedrooms: {property.bedrooms}, Bathrooms: {property.bathrooms}, Rent: ${property.rent}, Available: {'Yes' if property.available else 'No'}")

    def search_properties(self, min_bedrooms, max_rent):
        print(f"Properties with at least {min_bedrooms} bedrooms and rent less than ${max_rent}:")
        found = False
        for property in self.properties:
            if property.bedrooms >= min_bedrooms and property.rent <= max_rent and property.available:
                found = True
                print(f"Address: {property.address}, Bedrooms: {property.bedrooms}, Bathrooms: {property.bathrooms}, Rent: ${property.rent}")
        if not found:
            print("No properties found matching the criteria.")

    def mark_as_rented(self, address):
        for property in self.properties:
            if property.address == address:
                property.available = False
                print(f"Property at {address} marked as rented.")
                return
        print("Property not found.")

    def mark_as_available(self, address):
        for property in self.properties:
            if property.address == address:
                property.available = True
                print(f"Property at {address} marked as available.")
                return
        print("Property not found.")

# Main program
rental_manager = RentalManager()

while True:
    print("\nHouse Rental Management System")
    print("1. Add Rental Property")
    print("2. View Rental Properties")
    print("3. Search Rental Properties")
    print("4. Mark Property as Rented")
    print("5. Mark Property as Available")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        address = input("Enter property address: ")
        bedrooms = int(input("Enter number of bedrooms: "))
        bathrooms = int(input("Enter number of bathrooms: "))
        rent = float(input("Enter monthly rent amount: $"))
        rental_manager.add_property(address, bedrooms, bathrooms, rent)
    elif choice == '2':
        rental_manager.view_properties()
    elif choice == '3':
        min_bedrooms = int(input("Enter minimum number of bedrooms required: "))
        max_rent = float(input("Enter maximum rent amount: $"))
        rental_manager.search_properties(min_bedrooms, max_rent)
    elif choice == '4':
        address = input("Enter address of property to mark as rented: ")
        rental_manager.mark_as_rented(address)
    elif choice == '5':
        address = input("Enter address of property to mark as available: ")
        rental_manager.mark_as_available(address)
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
