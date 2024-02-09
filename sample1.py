def generate_hex_pattern(rows, cols):
    for y in range(rows):
        # Display the top half of the hexagon:
        for x in range(rows):
            print(r'/ \_', end='')
        print()

        # Display the bottom half of the hexagon:
        for x in range(rows):
            print(r'\_/ ', end='')
        print()

# Take input for the number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Generate the hexagonal pattern
generate_hex_pattern(rows, cols)
