class Plateau:
    """Represents the upper-right coordinates of the rectangular plateau."""
    
    def __init__(self, max_x: int, max_y: int):
        if max_x < 0 or max_y < 0:
            raise ValueError("Plateau coordinates must be non-negative.")
            
        self.max_x = max_x
        self.max_y = max_y

    def is_valid(self, x: int, y: int) -> bool:
        """Check if the given coordinates are within the plateau boundaries."""
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y
        
    def __repr__(self) -> str:
        return f"Plateau(max_x={self.max_x}, max_y={self.max_y})"
