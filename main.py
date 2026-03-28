import os
import re
from plateau import Plateau
from rover import Rover

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

def main():
    """Handles orchestrating the plateau simulation by reading inputs."""
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    try:
        with open(INPUT_FILE, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print("Error: Input file is empty.")
            return

        # Parse plateau limits
        plateau_args = lines[0].split()
        if len(plateau_args) != 2:
            raise ValueError("Invalid plateau dimensions format.")
            
        max_x = int(plateau_args[0])
        max_y = int(plateau_args[1])
        plateau = Plateau(max_x, max_y)

        results = []
        # Parse rovers sequentially
        for i in range(1, len(lines), 2):
            if i + 1 >= len(lines):
                raise ValueError(f"Expected commands for rover at line {i+1}, but found EOF.")
                
            # Use regex to handle spatial permutations of format gracefully
            match = re.match(r"^(\d+)\s+(\d+)\s*([A-Za-z])$", lines[i])
            if not match:
                raise ValueError(f"Invalid initial position format on line {i+1}: '{lines[i]}'")
                
            x = int(match.group(1))
            y = int(match.group(2))
            direction = match.group(3).upper()
            commands = lines[i+1].upper()
            
            # Additional validations
            if not plateau.is_valid(x, y):
                raise ValueError(f"Initial positions for rover at line {i+1} are out of bounds.")
                
            if not re.match(r"^[LRM]*$", commands):
                raise ValueError(f"Invalid command string on line {i+2}. Only L, R, M are allowed.")

            rover = Rover(x, y, direction, plateau)
            rover.execute(commands)
            results.append(rover.get_position())

        # Write the output to output.txt and print to console
        with open(OUTPUT_FILE, 'w') as f:
            for result in results:
                f.write(result + '\n')
                print(result)
                
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
