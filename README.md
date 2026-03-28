# Rover Navigation Simulator

A Python based simulator for controlling robotic rovers on a rectangular plateau.

## Problem Description
A squad of robotic rovers are to be landed on a rectangular plateau on Mars. A rover's state consists of its (x, y) coordinates and its heading (N, E, S, W). To control the rovers, ISRO sends strings of standard commands:
- `L`: turn left (90 degrees)
- `R`: turn right (90 degrees)
- `M`: move forward one grid point

## Project Structure
- `main.py`: Orchestrates the simulation reading from `input.txt` and writing to `output.txt`.
- `plateau.py`: Core logic ensuring the grid constraints are correctly enforced.
- `rover.py`: Definition of a Rover's state and behavior.
- `input.txt`: Typical commands sent to the rovers.
- `output.txt`: The resulting positions after simulation.
- `tests/test_rover.py`: Test suite validating rover behavior and error margins via Python's `unittest`.
- `README.md`: This documentation.

## How to run
Make sure you have Python 3 installed. No external packages are required.

1. Ensure the `input.txt` file is formulated correctly.
2. Run the main script:
   ```bash
   python main.py
   ```
3. The results will be printed to your console and correctly saved in `output.txt`.

### Sample Input
```text
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

### Sample Output
```text
1 3 N
5 1 E
```

## Testing Instructions
To verify correctness and prevent regression, run the `unittest` suite inside the `tests/` directory from the root of the project:
```bash
python -m unittest tests/test_rover.py
```

