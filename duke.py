import csv

# Input and output files
input_file = "raw_data.csv"
output_file = "clean_data.csv"

with open(input_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        # Skip empty rows
        if not any(row):
            continue
        # Capitalize all text cells
        cleaned_row = [cell.strip().title() if cell.isalpha() else cell for cell in row]
        writer.writerow(cleaned_row)

print(f"Cleaned data saved to {output_file}")
#guacalomete
#avocado