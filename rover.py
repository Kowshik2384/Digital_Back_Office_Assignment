from plateau import Plateau

class Rover:
    """Represents a robotic rover on the Mars plateau."""
    
    DIRECTIONS = ['N', 'E', 'S', 'W']
    
    def __init__(self, x: int, y: int, direction: str, plateau: Plateau):
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau
        
    def turn_left(self):
        """Spins the rover 90 degrees left."""
        idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(idx - 1) % 4]
        
    def turn_right(self):
        """Spins the rover 90 degrees right."""
        idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(idx + 1) % 4]
        
    def move(self):
        """Moves the rover forward one grid point in current direction."""
        new_x, new_y = self.x, self.y
        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'W':
            new_x -= 1
            
        if self.plateau.is_valid(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            # Prevent movement outside the plateau
            pass
            
    def execute(self, commands: str):
        """Executes a series of commands (L, R, M)."""
        valid_commands = {'L', 'R', 'M'}
        for cmd in commands:
            if cmd not in valid_commands:
                raise ValueError(f"Invalid command: {cmd}")
                
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'M':
                self.move()
                
    def get_position(self) -> str:
        """Returns the current position and direction of the rover."""
        return f"{self.x} {self.y} {self.direction}"
