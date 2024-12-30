from dataclasses import dataclass
from math import log
@dataclass
class MandelbrotSet:
    max_iterations: int
    escape_radius: float = 2

    def __contains__(self, c:complex) -> bool:
        self.stability(c) == 1
    
    def stability(self, c: complex, smooth=False, clamp=True) -> float:
        value = self.escape_count(c, smooth) / self.max_iterations
        return max(0, min(value, 1)) if clamp else value

    def escape_count(self, c:complex, smooth=False) -> int:
        z = 0
        for i in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > self.escape_radius:
                if smooth:
                    return i + 1 - log(log(abs(z))) / log(2)
                return i
        return self.max_iterations