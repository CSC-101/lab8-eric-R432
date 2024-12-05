import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide a file name as a command-line argument.")
        sys.exit(1)
    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    value1, value2 = map(float, line.split())
                    print(value1 + value2)
                except ValueError:
                    print(f"Could not convert values on line: {line.strip()}")
                except Exception as e:
                    print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    main()
