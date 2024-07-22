from .connect_mongo import client

# Select the database
db = client['stock_management']

# Define collections
products_collection = db['products']
stock_collection = db['stock']
invoices_collection = db['invoices']

def create_product(product_id, name, description, category, price):

    """Insert a new product into the products collection."""
    try:
        result = products_collection.insert_one({
            'product_id': product_id,
            'name': name,
            'category': category,
            'price': price,
            'description': description
        })
        print("Product inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Error inserting product:", e)

def get_product(product_id):
    """Fetch a product by its ID."""
    try:
        product = products_collection.find_one({'product_id': product_id})
        return product
    except Exception as e:
        print("Error fetching product:", e)

def update_stock(product_id, quantity, location):
    """Update stock information for a product."""
    try:
        result = stock_collection.update_one(
            {'product_id': product_id},
            {'$set': {'quantity': quantity, 'location': location}},
            upsert=True
        )
        print("Stock updated:", result.modified_count)
    except Exception as e:
        print("Error updating stock:", e)

def create_invoice(invoice_id, date, items):
    """Create a new invoice."""
    try:
        result = invoices_collection.insert_one({
            'invoice_id': invoice_id,
            'date': date,
            'items': items
        })
        print("Invoice created with ID:", result.inserted_id)
    except Exception as e:
        print("Error creating invoice:", e)
