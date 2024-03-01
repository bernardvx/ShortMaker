import csv

def remove_duplicates(input_file, output_file):
    # Set to store unique rows
    unique_rows = set()

    # Read input file and remove duplicates
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip header row
        unique_rows.add(tuple(header))  # Include header row in unique rows
        for row in reader:
            unique_rows.add(tuple(row))

    # Write unique rows to output file
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(unique_rows)

    print("Duplicates removed and unique rows written to", output_file)


# Usage example
input_file = 'ids_add.csv'
output_file = 'ids_finalv3.csv'
remove_duplicates(input_file, output_file)
