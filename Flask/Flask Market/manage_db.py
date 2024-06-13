from app import db, Item

def create_db():
    """Creates the database and the tables."""
    db.create_all()
    print("Database and tables created.")

def add_item(name, price, barcode, description):
    """Adds a new item to the database."""
    new_item = Item(name=name, price=price, barcode=barcode, description=description)
    db.session.add(new_item)
    db.session.commit()
    print(f"Item '{name}' added to the database.")

def list_items():
    """Lists all items in the database."""
    items = Item.query.all()
    for item in items:
        print(item)

if __name__ == '__main__':
    # Example usage
    create_db()  # Creates the database
    add_item("Laptop", 1500, "123456789012", "A high-end gaming laptop.")
    add_item("Smartphone", 800, "987654321098", "A latest model smartphone.")
    list_items()  # Lists all items
