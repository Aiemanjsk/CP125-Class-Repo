# Lab 08 Exercise 5: Sales Summary
# Write your code below:

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    # TODO: Implement this function
    import csv
    sales = open(input_file, mode = "r", newline = "")
    summary = open(output_file, "w")
    read_sales = csv.reader(sales)
    next(read_sales)
    total_revenue = 0
    count = 0
    highest_revenue = 0
    lowest_revenue = float("inf")
    for summarize in read_sales:
        revenue = float(summarize[1]) * float(summarize[2])
        total_revenue += revenue
        count += 1
        if revenue > highest_revenue:
            highest_revenue = revenue
        if revenue < lowest_revenue:
            lowest_revenue = revenue    
    average = total_revenue / count
    summary.write(f"Total Revenue: ${total_revenue:.2f}\n")
    summary.write(f"Average Revenue: ${average:.2f}\n")
    summary.write(f"Highest Revenue: ${highest_revenue:.2f}\n")
    summary.write(f"Lowest Revenue: ${lowest_revenue:.2f}\n")
    sales.close()
    summary.close()
    return (total_revenue, average, highest_revenue, lowest_revenue)
    pass


# Test your code here
result = summarize_sales("Labs/lab08/exercise5/data/sales.csv", "Labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
