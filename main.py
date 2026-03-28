import os
import re
from plateau import Plateau
from rover import Rover

def main():
    """Handles orchestrating the plateau simulation by reading inputs."""
    input_file = "input.txt"
    output_file = "output.txt"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    try:
        with open(input_file, 'r') as f:
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
                print(f"Warning: Expected commands for rover at line {i+1}, but found none.")
                break
                
            # Use regex to handle both "1 2 N" and "1 2N" formats gracefully
            match = re.match(r"^(\d+)\s+(\d+)\s*([A-Za-z])$", lines[i])
            if not match:
                raise ValueError(f"Invalid initial position format on line {i+1}: '{lines[i]}'")
                
            x = int(match.group(1))
            y = int(match.group(2))
            direction = match.group(3).upper()
            commands = lines[i+1].upper()
            
            if direction not in Rover.DIRECTIONS:
                raise ValueError(f"Invalid direction '{direction}' on line {i+1}.")

            rover = Rover(x, y, direction, plateau)
            rover.execute(commands)
            results.append(rover.get_position())

        # Write the output to output.txt and print to console
        with open(output_file, 'w') as f:
            for result in results:
                f.write(result + '\n')
                print(result)
                
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
