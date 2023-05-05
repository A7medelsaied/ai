import random

class SnakeGame:
    def _init_(self, size):
        self.size = size
        self.snake = [(random.randint(0, size-1), random.randint(0, size-1))]
        self.apple = (random.randint(0, size-1), random.randint(0, size-1))
        self.direction = random.choice(["up", "down", "left", "right"])
        self.game_over = False
    
    def get_state(self):
        head = self.snake[0]
        state = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i, j) == head:
                    row.append("H")
                elif (i, j) == self.apple:
                    row.append("A")
                elif (i, j) in self.snake:
                    row.append("S")
                else:
                    row.append(" ")
            state.append(row)
        return state
    
    def move(self):
        def dfs(game, depth):
            if depth == 0 or game.game_over:
                return None

            directions = ["up", "down", "left", "right"]
            random.shuffle(directions)
            for direction in directions:
                game.direction = direction
                new_state = game.get_state()
                if game.snake[0] == game.apple:
                    return direction
                result = dfs(game, depth-1)
                if result is not None:
                    return result

            return None
        
        head = self.snake[0]
        direction = dfs(self, 10)
        if direction is not None:
            self.direction = direction
        else:
            self.game_over = True
        
        if self.game_over:
            return
        
        if self.direction == "up":
            new_head = (head[0]-1, head[1])
        elif self.direction == "down":
            new_head = (head[0]+1, head[1])
        elif self.direction == "left":
            new_head = (head[0], head[1]-1)
        elif self.direction == "right":
            new_head = (head[0], head[1]+1)
        
        if new_head in self.snake or new_head[0] < 0 or new_head[0] >= self.size or new_head[1] < 0 or new_head[1] >= self.size:
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)
        if new_head == self.apple:
            self.apple = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        else:
            self.snake.pop()
    
    def step(self):
        self.move()
        if not self.game_over:
            state = self.get_state()
            return state
        else:
            return None

game = SnakeGame()
while not game.game_over:
    state = game.get_state()
    print("".join(["".join(row)+"\n" for row in state]))
    direction = dfs(game, 10)
    if direction is not None:
        game.direction = direction
    else:
        game.game_over = True
print("Game over!")
