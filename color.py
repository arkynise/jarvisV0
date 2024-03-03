import time

# Function to write color data to a file
def write_color(color_data):
    with open("color.txt", "w") as file:
        file.write(color_data)

# Example usage
