import csv
import random
import datetime

def generate_sales_data():
    # Define column headers
    headers = ['Order ID', 'Order Date', 'Customer ID', 'Customer Name', 'Product ID', 'Product Name', 'Quantity', 'Price', 'City', 'State', 'Country', 'Total Sales']

    # Create a dictionary with city and state pairs
    city_state_pairs = {
        "New York": "NY",
        "Los Angeles": "CA",
        "Chicago": "IL",
        "Houston": "TX",
        "Phoenix": "AZ",
        "Las Vegas": "NV",
        "San Francisco": "CA",
        "San Diego": "CA",
        "San Antonio": "TX",
        "Austin": "TX",
        "Seattle": "WA",
        "Denver": "CO",
        "Salt Lake": "UT",
        "Boston": "MA",
        "Miami": "FL",
        "Atlanta": "GA"
    }

    # Create a dictionary with product categories and descriptive names
    product_categories = {
        "Electronics": ["Computer", "Laptop", "Smartphone", "Tablet", "TV"],
        "Clothing": ["Men's Shirt", "Women's Dress", "Jeans", "Shoes", "Accessories"],
        "Home Goods": ["Furniture", "Kitchenware", "Bedding", "Decor", "Appliances"]
    }

    # Generate random data
    data = []
    for i in range(50):
        order_id = f"ORDER-{i+1}"
        order_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365))
        customer_id = f"CUST-{random.randint(1000, 2000)}"
        customer_name = f"Customer {random.randint(1, 100)}"
        product_id = f"PROD-{random.randint(100, 500)}"
        category = random.choice(list(product_categories.keys()))
        product_name = random.choice(product_categories[category])
        quantity = random.randint(1, 10)
        price = random.uniform(10, 100)
        city = random.choice(list(city_state_pairs.keys()))
        state = city_state_pairs[city]
        country = "USA"
        total_sales = quantity * price
        data.append([order_id, order_date.strftime('%Y-%m-%d'), customer_id, customer_name, product_id, product_name, quantity, price, city, state, country, total_sales])

    # Write data to CSV file
    with open('sales_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    generate_sales_data()