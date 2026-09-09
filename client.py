import math

class LloydSwarmCoverage:
    """Distributed Lloyd's Algorithm for Swarm Area Coverage."""
    def __init__(self, region_bounds=(0, 100, 0, 100)):
        self.bounds = region_bounds
        self.robots = {}

    def add_robot(self, rid, pos):
        self.robots[rid] = list(pos)

    def iterate_lloyd(self, grid_res=10):
        xmin, xmax, ymin, ymax = self.bounds
        cells = {rid: [] for rid in self.robots}

        for x in range(int(xmin), int(xmax) + 1, grid_res):
            for y in range(int(ymin), int(ymax) + 1, grid_res):
                best_rid = min(self.robots.keys(), key=lambda r: math.hypot(x - self.robots[r][0], y - self.robots[r][1]))
                cells[best_rid].append((x, y))

        new_positions = {}
        for rid, pts in cells.items():
            if pts:
                cx = sum(p[0] for p in pts) / len(pts)
                cy = sum(p[1] for p in pts) / len(pts)
                self.robots[rid] = [round(cx, 2), round(cy, 2)]
            new_positions[rid] = self.robots[rid]
        return new_positions
