"""
Snake Game
A classic Snake game implemented using Pygame
All text and comments are in English
"""

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Direction Constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game Settings
FPS = 10
INITIAL_SPEED = 10


class Snake:
    """Snake class to manage snake behavior"""
    
    def __init__(self):
        """Initialize the snake"""
        self.length = 3
        self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0
        
    def get_head_position(self):
        """Get the position of snake's head"""
        return self.positions[0]
    
    def update(self):
        """Update snake position"""
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), 
               (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT)
        
        # Check if snake collides with itself
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        """Reset the snake to initial state"""
        self.length = 3
        self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
    
    def render(self, surface):
        """Render the snake on the surface"""
        for p in self.positions:
            pygame.draw.rect(surface, self.color, 
                           (p[0], p[1], GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, DARK_GREEN, 
                           (p[0], p[1], GRID_SIZE, GRID_SIZE), 1)
    
    def handle_keys(self):
        """Handle keyboard input for snake direction"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT


class Food:
    """Food class to manage food behavior"""
    
    def __init__(self):
        """Initialize food"""
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()
    
    def randomize_position(self):
        """Randomize food position"""
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                        random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
    
    def render(self, surface):
        """Render food on the surface"""
        pygame.draw.rect(surface, self.color, 
                        (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, (200, 0, 0), 
                        (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE), 1)


class Game:
    """Main game class"""
    
    def __init__(self):
        """Initialize the game"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.game_over = False
        self.paused = False
        
    def check_collision(self):
        """Check if snake eats food"""
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.snake.score += 10
            self.food.randomize_position()
            
            # Make sure food doesn't appear on snake's body
            while self.food.position in self.snake.positions:
                self.food.randomize_position()
    
    def check_game_over(self):
        """Check if game is over"""
        head = self.snake.get_head_position()
        
        # Check wall collision
        if (head[0] < 0 or head[0] >= WINDOW_WIDTH or 
            head[1] < 0 or head[1] >= WINDOW_HEIGHT):
            return True
        
        # Check self collision
        if head in self.snake.positions[1:]:
            return True
        
        return False
    
    def draw_grid(self):
        """Draw grid lines on the screen"""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y))
    
    def draw_score(self):
        """Draw score on the screen"""
        score_text = self.font.render(f'Score: {self.snake.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw instructions
        instructions = [
            'Arrow Keys: Move',
            'P: Pause',
            'R: Restart',
            'ESC: Quit'
        ]
        
        for i, instruction in enumerate(instructions):
            text = self.small_font.render(instruction, True, WHITE)
            self.screen.blit(text, (WINDOW_WIDTH - 150, 10 + i * 25))
    
    def draw_game_over(self):
        """Draw game over screen"""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font.render('GAME OVER!', True, RED)
        score_text = self.font.render(f'Final Score: {self.snake.score}', True, WHITE)
        restart_text = self.small_font.render('Press R to Restart or ESC to Quit', True, WHITE)
        
        self.screen.blit(game_over_text, 
                        (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 
                         WINDOW_HEIGHT // 2 - 50))
        self.screen.blit(score_text, 
                        (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 
                         WINDOW_HEIGHT // 2))
        self.screen.blit(restart_text, 
                        (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 
                         WINDOW_HEIGHT // 2 + 50))
    
    def draw_pause(self):
        """Draw pause screen"""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font.render('PAUSED', True, WHITE)
        continue_text = self.small_font.render('Press P to Continue', True, WHITE)
        
        self.screen.blit(pause_text, 
                        (WINDOW_WIDTH // 2 - pause_text.get_width() // 2, 
                         WINDOW_HEIGHT // 2 - 20))
        self.screen.blit(continue_text, 
                        (WINDOW_WIDTH // 2 - continue_text.get_width() // 2, 
                         WINDOW_HEIGHT // 2 + 20))
    
    def reset_game(self):
        """Reset the game"""
        self.snake.reset()
        self.food.randomize_position()
        self.game_over = False
        self.paused = False
    
    def run(self):
        """Main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        self.reset_game()
                    elif event.key == pygame.K_p and not self.game_over:
                        self.paused = not self.paused
                    elif not self.game_over and not self.paused:
                        if event.key == pygame.K_UP and self.snake.direction != DOWN:
                            self.snake.direction = UP
                        elif event.key == pygame.K_DOWN and self.snake.direction != UP:
                            self.snake.direction = DOWN
                        elif event.key == pygame.K_LEFT and self.snake.direction != RIGHT:
                            self.snake.direction = LEFT
                        elif event.key == pygame.K_RIGHT and self.snake.direction != LEFT:
                            self.snake.direction = RIGHT
            
            # Update game state
            if not self.game_over and not self.paused:
                self.snake.update()
                self.check_collision()
                
                if self.check_game_over():
                    self.game_over = True
            
            # Draw everything
            self.screen.fill(BLACK)
            self.draw_grid()
            self.snake.render(self.screen)
            self.food.render(self.screen)
            self.draw_score()
            
            if self.game_over:
                self.draw_game_over()
            elif self.paused:
                self.draw_pause()
            
            pygame.display.update()
            self.clock.tick(FPS)


def main():
    """Main function to run the game"""
    print("=" * 50)
    print("Snake Game")
    print("=" * 50)
    print("\nControls:")
    print("  Arrow Keys - Move the snake")
    print("  P - Pause/Resume game")
    print("  R - Restart game")
    print("  ESC - Quit game")
    print("\nObjective:")
    print("  Eat the red food to grow and score points!")
    print("  Avoid hitting the walls or yourself!")
    print("\n" + "=" * 50)
    print("Starting game...")
    print("=" * 50 + "\n")
    
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
