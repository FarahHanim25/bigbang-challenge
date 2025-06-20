import json

def generate_bigbang_array():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("BIGBANG")
        elif i % 3 == 0:
            result.append("BIG")
        elif i % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(i))

    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    generate_bigbang_array()

# This script generates an array of numbers from 1 to 100,
# replacing multiples of 3 with "BIG", multiples of 5 with "BANG",
# and multiples of both 3 and 5 with "BIGBANG".
# The result is saved to a file named output.json in the current directory.
# To run the script, simply execute it in a Python environment.