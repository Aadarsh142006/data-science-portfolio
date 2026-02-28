from concurrent.futures import ThreadPoolExecutor

# Function to process each number
def process_number(n):
    return n * n  # square the number

def main():
    numbers = [1, 2, 3, 4, 5]  # simple list

    # Use ThreadPoolExecutor to process the list
    with ThreadPoolExecutor(max_workers=3) as executor:
        # map() runs the function on each element in parallel
        results = list(executor.map(process_number, numbers))

    print("Processed results:", results)

if __name__ == "__main__":
    main()