from plateau import Plateau

class Rover:
    """Represents a robotic rover on the Mars plateau."""
    
    DIRECTIONS = {'N', 'E', 'S', 'W'}
    
    LEFT_TURNS = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    RIGHT_TURNS = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    
    MOVES = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    
    def __init__(self, x: int, y: int, direction: str, plateau: Plateau):
        if direction not in self.DIRECTIONS:
            raise ValueError(f"Invalid direction: '{direction}'. Must be one of {self.DIRECTIONS}")
            
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau
        
    def turn_left(self):
        """Spins the rover 90 degrees left."""
        self.direction = self.LEFT_TURNS[self.direction]
        
    def turn_right(self):
        """Spins the rover 90 degrees right."""
        self.direction = self.RIGHT_TURNS[self.direction]
        
    def move(self):
        """Moves the rover forward one grid point in current direction."""
        dx, dy = self.MOVES[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
            
        if self.plateau.is_valid(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            # Reached boundary of the plateau, ignoring movement command.
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
