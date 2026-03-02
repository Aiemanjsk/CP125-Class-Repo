# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    input1 = open(file1, "r")
    input2 = open(file2, "r")
    output = open(output_file, "w")
    names1 = input1.readlines()
    names2 = input2.readlines()
    combined_list = names1 + names2
    combined_set = set()
    for name in combined_list:
        combined_set.add(name.strip())
    combined_name  = sorted(combined_set)


    for name in combined_name:
        output.write(name + "\n")  

    input1.close()
    input2.close()
    output.close()

    return len(combined_name)


    # TODO: Implement this function
    pass


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
