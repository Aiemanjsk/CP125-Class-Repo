# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function
    input1 = open(products_file, "r")
    input2 = open(order_file, "r")
    output = open(output_file, "w")

    names1 = input1.readlines()
    names2 = input2.readlines()

    price_dict = {}
    cost_list = []
    grand_total = 0

    for line in names1[1:]:
        data = line.strip().split(",")
        product_id = data[0]
        price = float(data[2])
        price_dict[product_id] = price

    output.write("product_id,total_cost\n")

    for quantity in names2[1:]:
        data = quantity.strip().split(",")
        product_id = data[0]
        quantity = int(data[1])

        price = price_dict[product_id]
        total_cost = price * quantity
        grand_total += total_cost

        cost_list.append(total_cost)

        output.write(product_id + "," + format(total_cost, ".2f") + "\n")

    input1.close()
    input2.close()
    output.close()

    return grand_total


    pass


# Test your code here
result = calculate_order_total("Labs/lab08/exercise3/data/products.csv", "Labs/lab08/exercise3/data/order.csv", "Labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
