# from an image extract the floating point numbers and group them by a wayout
# group them as a value of the floating point number that is close to the another in the same wayout
import re

def extract_numbers(image_path):
    """Extract floating-point numbers from an image."""
    
    # Use a regular expression to find all numbers in the image
    with open(image_path, 'rb') as file:
        image_data = file.read()
        numbers = re.findall(r'\d+\.\d+', image_data.decode(encoding='utf-8'))
    
    return numbers

def group_numbers(numbers):
    """Group numbers by proximity."""

    grouped_numbers = {'positive': [], 'negative': [], 'zero': []}

    for number in numbers:
        value = float(number)
        if value > 0:
            grouped_numbers['positive'].append(value)
        elif value < 0:
            grouped_numbers['negative'].append(value)
        else:
            grouped_numbers['zero'].append(value)

    return grouped_numbers

# Example usage
image_path = 'C:/image_pixel_coordinates_path'
numbers = extract_numbers(image_path)
grouped_numbers = group_numbers(numbers)

print(f"Positive numbers: {grouped_numbers['positive']}")
print(f"Negative numbers: {grouped_numbers['negative']}")
print(f"Zero numbers: {grouped_numbers['zero']}")
