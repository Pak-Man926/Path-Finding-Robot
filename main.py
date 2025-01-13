import random

class PathfindingRobotGame:
    def __init__(self, grid_size, start, goal):
        self.grid_size = grid_size
        self.position = start
        self.goal = goal
        self.environment = self.generate_environment()

    def generate_environment(self):
        grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        # Place random obstacles ('X') on the grid
        for _ in range(int(self.grid_size * 1.5)):
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            if (x, y) != self.position and (x, y) != self.goal:
                grid[x][y] = 'X'  # Mark obstacle
        return grid

    def display_environment(self):
        grid_copy = [row[:] for row in self.environment]
        # Mark the robot's position with 'R' and the goal with 'G'
        grid_copy[self.position[0]][self.position[1]] = 'R'
        grid_copy[self.goal[0]][self.goal[1]] = 'G'
        for row in grid_copy:
            print(' '.join(row))
        print("\n")

    def is_obstacle(self, x, y):
        # Check if the position contains an obstacle
        return self.environment[x][y] == 'X'

    def is_valid_move(self, x, y):
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size and not self.is_obstacle(x, y)

    def prompt_user_for_move(self):
        print("Enter your move (up, down, left, right):")
        while True:
            move = input().lower()
            x, y = self.position
            if move == 'up' and self.is_valid_move(x - 1, y):
                return 'up'
            elif move == 'down' and self.is_valid_move(x + 1, y):
                return 'down'
            elif move == 'left' and self.is_valid_move(x, y - 1):
                return 'left'
            elif move == 'right' and self.is_valid_move(x, y + 1):
                return 'right'
            else:
                print("Invalid move! Please try again.")

    def actuators(self, action):
        x, y = self.position
        if action == 'up':
            self.position[0] -= 1
        elif action == 'down':
            self.position[0] += 1
        elif action == 'left':
            self.position[1] -= 1
        elif action == 'right':
            self.position[1] += 1

    def run(self):
        steps = 0
        while self.position != self.goal:
            self.display_environment()
            print(f"Current Position: {self.position}, Goal: {self.goal}")
            action = self.prompt_user_for_move()
            self.actuators(action)
            steps += 1
        print(f"Congratulations! You reached the goal in {steps} steps!")


# Test the interactive pathfinding robot game
robot_game = PathfindingRobotGame(grid_size=5, start=[0, 0], goal=[4, 4])
robot_game.run()
