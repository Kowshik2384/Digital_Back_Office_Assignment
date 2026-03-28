class Plateau:
    """Represents the upper-right coordinates of the rectangular plateau."""
    
    def __init__(self, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = 0
        self.min_y = 0

    def is_valid(self, x: int, y: int) -> bool:
        """Check if the given coordinates are within the plateau boundaries."""
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y
