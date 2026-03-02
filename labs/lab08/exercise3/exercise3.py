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
    for i in range (len(products_file)):
        total_cost = price * quantity
        cost_list.add(total_cost)

    input1.close()
    input2.close()
    output.close()
    return cost_list


    pass


# Test your code here
result = calculate_order_total("Labs/lab08/exercise3/data/products.csv", "Labs/lab08/exercise3/data/order.csv", "Labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
