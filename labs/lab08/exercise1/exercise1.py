# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')

    count = 0

    for line in infile:
        parts = line.split(" ")
        
        if len(parts) == 2:
            student_id = parts[0]
            score = int(parts[1])

            if score >= 80:
                outfile.write(student_id + " " + str(score) + "\n")
                count += 1

    infile.close()
    outfile.close()

    return count


# Test your code here
result = filter_passing_scores("Labs/lab08/exercise1/data/scores.txt", "Labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
