# Retail Sales Dashboard Using CSV and Matplotlib

import csv
import os
import matplotlib.pyplot as plt

filename = "retail_sales.csv"

# Create sample CSV file
if not os.path.exists(filename):
    data = [
        ["Product", "Quantity", "Price"],
        ["Laptop", 5, 45000],
        ["Mobile", 10, 15000],
        ["Headphones", 15, 2000],
        ["Keyboard", 8, 1000],
        ["Mouse", 12, 500]
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Read CSV file
products = []
sales = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        revenue = quantity * price

        products.append(product)
        sales.append(revenue)

# Display sales report
total_sales = sum(sales)

print("\nRETAIL SALES REPORT")
print("-------------------")

for i in range(len(products)):
    print(products[i], ":", sales[i])

print("\nTotal Sales:", total_sales)

# Bar Chart
plt.figure(figsize=(8, 5))

plt.bar(products, sales)

plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Revenue")

plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%"
)

plt.title("Product Sales Distribution")

plt.show()