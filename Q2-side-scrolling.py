import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  # New color for Level 3 enemies

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Game Menu")

# Font settings
font = pygame.font.Font(None, 40)

# Utility function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)



# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT - 70)
        self.speed_x = 0
        self.speed_y = 0
        self.jump_power = -15
        self.gravity = 0.8
        self.jumping = False
        self.health = 80
        self.projectiles = pygame.sprite.Group()

    def update(self):
        self.speed_y += self.gravity
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Boundary conditions
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom >= SCREEN_HEIGHT - 10:
            self.rect.bottom = SCREEN_HEIGHT - 10
            self.speed_y = 0
            self.jumping = False

        # Update projectiles
        self.projectiles.update()

    def jump(self):
        if not self.jumping:
            self.speed_y = self.jump_power
            self.jumping = True

    def shoot(self):
        # Create a standard projectile
        projectile_instance = Projectile(self.rect.centerx, self.rect.centery, self.speed_x)
        self.projectiles.add(projectile_instance)
        all_sprites.add(projectile_instance)  # Ensure all_sprites is defined in your scope

    def shoot_up(self):
        # Create an upward projectile
        upward_projectile = VerticalProjectile(self.rect.centerx, self.rect.top)
        self.projectiles.add(upward_projectile)
        all_sprites.add(upward_projectile)

    def handle_shooting(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            self.shoot()  # Standard shoot
        if keys[pygame.K_UP]:  # Shoot upward
            self.shoot_up()

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Handle player death (if applicable)


# Define the Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x):
        super().__init__()
        self.image = pygame.Surface((10, 5))  # Create a simple projectile surface
        self.image.fill((255, 0, 0))  # Color the projectile red
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x + 10  # Adjust speed as needed
        self.damage = 10  # Damage dealt by this projectile

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x > SCREEN_WIDTH:  # Remove if it goes off the right side
            self.kill()



# Define the VerticalProjectile class
class VerticalProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = -10  # Speed of the projectile (moving upwards)
        self.damage = 10  # Damage dealt by this projectile

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0: 
            self.kill()



# Define the RegularEnemyf classes
class RegularEnemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((80, 120))  # Size of the enemy
        self.image.fill(GREEN)  # Color of the enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)  # Start off-screen to the right
        self.rect.y = SCREEN_HEIGHT - 120  # Set Y position
        self.speed_x = -3  # Speed of the enemy moving left

        # Add health attribute
        self.health = 100  # Initial health value
        self.player = player  # Store the player reference

    def update(self):
        # Move the enemy left
        self.rect.x += self.speed_x
        
        # Check if the enemy has moved off the left side of the screen
        if self.rect.right < 0:
            self.kill()  # Remove the enemy if it goes off-screen

        # Check for collision with the player
        if pygame.sprite.collide_rect(self, self.player):  # Check for collision with the player
            # Implement damage logic on collision
            self.health -= 10  # Example: reduce enemy health if it collides with player
            if self.health <= 0:
                self.kill()  # Kill the enemy if health is zero

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Handle enemy death




class FastEnemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((80, 120))  # Size of the enemy
        self.image.fill(YELLOW)  # Color of the enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)  # Start off-screen to the right
        self.rect.y = SCREEN_HEIGHT - 120  # Set Y position
        self.speed_x = -5  # Speed of the enemy moving left
        
        # Add health attribute
        self.health = 10  # Initial health value for FastEnemy
        self.player = player  # Store the player reference for collision detection

    def update(self):
        # Move the enemy left
        self.rect.x += self.speed_x
        
        # Check for collision with the player
        if pygame.sprite.collide_rect(self, self.player):  # Check for collision with the player
            self.take_damage(10)  # Damage the enemy upon collision with the player

        # Remove enemy if it goes off screen
        if self.rect.right < 0:
            self.kill()  # Remove the enemy if it goes off-screen

    def take_damage(self, amount):
        """Reduce health by the amount of damage taken."""
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove the enemy if health is zero or below



class StrongEnemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((80, 120))  # Size of the enemy
        self.image.fill(ORANGE)  # Color of the enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)  # Start off-screen to the right
        self.rect.y = SCREEN_HEIGHT - 120  # Set Y position
        self.speed_x = -2  # Speed of the enemy moving left
        
        # Add health attribute
        self.health = 60  # Initial health value for StrongEnemy
        self.player = player  # Store the player reference for collision detection

    def update(self):
        # Move the enemy left
        self.rect.x += self.speed_x
        
        # Check for collision with the player
        if pygame.sprite.collide_rect(self, self.player):  # Check for collision with the player
            self.take_damage(10)  # Damage the enemy upon collision with the player

        # Remove enemy if it goes off screen
        if self.rect.right < 0:
            self.kill()  # Remove the enemy if it goes off-screen

    def take_damage(self, amount):
        """Reduce health by the amount of damage taken."""
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove the enemy if health is zero or below



class AggressiveEnemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Size of the enemy
        self.image.fill(RED)  # Fill with red color
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)  # Random X position
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)  # Random Y position
        self.speed_x = 3  # Speed of the enemy
        self.health = 50  # Initial health value for AggressiveEnemy

        self.player = player  # Store the player reference for tracking

    def update(self):
        # Chase the player
        if self.player.rect.x < self.rect.x:
            self.rect.x -= self.speed_x
        elif self.player.rect.x > self.rect.x:
            self.rect.x += self.speed_x

        if self.player.rect.y < self.rect.y:
            self.rect.y -= self.speed_x
        elif self.player.rect.y > self.rect.y:
            self.rect.y += self.speed_x

        # Check boundaries to keep the enemy on screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

        # Check for collision with the player
        if pygame.sprite.collide_rect(self, self.player):  # Check for collision with the player
            self.take_damage(10)  # Damage the enemy upon collision with the player

    def take_damage(self, amount):
        """Reduce health by the amount of damage taken."""
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove the enemy if health is zero or below

class BossEnemy(pygame.sprite.Sprite):
    def __init__(self, boss_projectiles):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, 100)
        
        # Boss properties
        self.health = 200
        self.shoot_timer = 0
        self.boss_projectiles = boss_projectiles

    def update(self):
        """Update the boss enemy state, including shooting logic."""
        self.shoot_timer += 1
        if self.shoot_timer > 60:  # Adjust the shooting frequency here
            self.shoot()
            self.shoot_timer = 0

    def shoot(self):
        """Create and add different types of projectiles."""
        # Shoot a spread attack
        self.shoot_spread()

        # Shoot one projectile directly down
        self.shoot_straight_down()

        # Randomly shoot raining projectiles
        if random.randint(0, 1):  # 50% chance to shoot raining projectiles
            self.shoot_rain()

    def shoot_spread(self):
        """Create and add multiple projectiles in a spread pattern."""
        num_projectiles = 10  # Number of projectiles in the spread
        spread_range = 5  # Range for horizontal speeds (controls how far left/right projectiles move)

        for i in range(num_projectiles):
            # Vary the horizontal speed between -spread_range to +spread_range
            x_speed = -spread_range + i * (2 * spread_range / (num_projectiles - 1))
            projectile = BossProjectile(self.rect.centerx, self.rect.bottom, x_speed)
            all_sprites.add(projectile)  # Add to all sprites
            self.boss_projectiles.add(projectile)  # Add to the boss_projectiles group

    def shoot_straight_down(self):
        """Shoot one projectile directly down."""
        projectile = BossProjectile(self.rect.centerx, self.rect.bottom, 0)  # No horizontal speed
        all_sprites.add(projectile)
        self.boss_projectiles.add(projectile)

    def shoot_rain(self):
        """Shoot multiple projectiles that rain down from above."""
        num_rain_projectiles = 5  # Number of raining projectiles
        for _ in range(num_rain_projectiles):
            x_position = random.randint(0, SCREEN_WIDTH)  # Random x position
            projectile = BossProjectile(x_position, 0, 0)  # Start from the top
            all_sprites.add(projectile)
            self.boss_projectiles.add(projectile)

    def take_damage(self, amount):
        """Reduce the boss health by the specified amount."""
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove the boss from all sprites if defeated
            boss_defeated()  # Call your method to handle boss defeat


class BossProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, x_speed=0):
        super().__init__()
        self.image = pygame.Surface((10, 20))  # Projectile size
        self.image.fill((0, 255, 0))  # Projectile color (green)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Set initial position at x and y

        # Speed along the x-axis (horizontal)
        self.x_speed = x_speed

    def update(self):
        """Update the projectile's position."""
        self.rect.y += 10  # Move the projectile downwards
        
        # Move the projectile horizontally
        self.rect.x += self.x_speed

        # Remove the projectile if it goes off-screen (either x or y bounds)
        if self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()  # Remove the projectile if it is off the screen




def draw_health_bar(boss, screen):
    bar_width = 200
    bar_height = 20
    fill = (boss.health / 200) * bar_width
    border_rect = pygame.Rect(SCREEN_WIDTH / 2 - bar_width / 2, 20, bar_width, bar_height)
    fill_rect = pygame.Rect(SCREEN_WIDTH / 2 - bar_width / 2, 20, fill, bar_height)
    pygame.draw.rect(screen, RED, fill_rect)
    pygame.draw.rect(screen, BLACK, border_rect, 2)

# Define the Collectible class
class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)
        self.rect.y = SCREEN_HEIGHT - 70

    def update(self):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.kill()


def level_1():
    screen.fill(WHITE)

    player = Player()  # Create the player instance
    all_sprites.add(player)  # Add the player to the sprite group

    # Create enemies (10 total), ensuring they spawn away from the player
    enemies = pygame.sprite.Group()
    
    for i in range(10):
        enemy = RegularEnemy(player)  # Pass player instance to RegularEnemy
        enemy.rect.x = random.randint(100, SCREEN_WIDTH - 100)  # Adjust spawn positions
        enemy.rect.y = 500   # Adjust spawn positions
        enemies.add(enemy)
        all_sprites.add(enemy)

    running = True
    defeated_enemies = 0  # Counter for defeated enemies
    boss_fight = False  # Flag to start the boss fight
    boss = None  # Boss object
    boss_projectiles = pygame.sprite.Group()

    while running:
        # Clear the screen
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_f:
                    player.shoot()  # Shoot forward
                if event.key == pygame.K_g:  # Key for shooting upwards
                    player.shoot_up()  # Call the shoot_up method

        # Player movement
        keys = pygame.key.get_pressed()
        player.speed_x = 0  # Reset speed by default
        if keys[pygame.K_LEFT]:
            player.speed_x = -5
        elif keys[pygame.K_RIGHT]:
            player.speed_x = 5

        # Update all sprites
        all_sprites.update()

        # Check for projectile collisions with enemies
        for projectile in player.projectiles:
            hit_enemies = pygame.sprite.spritecollide(projectile, enemies, True)
            if hit_enemies:
                projectile.kill()  # Destroy the projectile
                defeated_enemies += len(hit_enemies)  # Increment defeated enemies count

        # Check for player collisions with regular enemies
        if pygame.sprite.spritecollide(player, enemies, True):
            player.health -= 10  # Decrease health on collision
            defeated_enemies += 1  # Increment defeated enemies count
            if player.health <= 0:
                game_over()

        # Remove enemies that reach the bottom of the screen
        for enemy in enemies:
            if enemy.rect.y > SCREEN_HEIGHT:
                enemy.kill()  # Remove enemy from all sprites
                defeated_enemies += 1  # Increment defeated enemies count

        # Display player's health
        draw_text(f'Health: {player.health}', font, BLACK, screen, SCREEN_WIDTH - 100, 30)

        # Start boss fight only after all enemies are defeated
        if not enemies and not boss_fight:  # Ensure no remaining enemies
            boss_fight = True
            boss = BossEnemy(boss_projectiles)  # Initialize boss
            all_sprites.add(boss)

        # Check for player collisions with the boss
        if boss and pygame.sprite.collide_rect(player, boss):
            player.health -= 10  # Decrease player health on boss collision
            if player.health <= 0:
                game_over()

        # Check for projectile collisions with the boss
        if boss:
            for projectile in player.projectiles:
                if pygame.sprite.collide_rect(projectile, boss):
                    projectile.kill()  # Destroy the projectile
                    boss.health -= 10  # Decrease boss health on hit
                    if boss.health <= 0:
                        boss_defeated()

            # Boss attack logic
            for projectile in boss_projectiles:  # Check for each projectile fired by the boss
                if pygame.sprite.collide_rect(player, projectile):  # Check if the player collides with the projectile
                    player.health -= 5  # Decrease player health on collision with projectile
                    projectile.kill()  # Destroy the projectile after collision
                    if player.health <= 0:
                        game_over()

        # Draw the boss health bar if the boss is present
        if boss:
            draw_health_bar(boss, screen)

        # Draw all sprites
        all_sprites.draw(screen)

        # Refresh the display
        pygame.display.flip()
        pygame.time.delay(30)



def level_2():
    screen.fill(WHITE)

    player = Player()  # Create the player instance
    all_sprites.add(player)  # Add the player to the sprite group

    # Create enemies (20 total), ensuring they spawn at the same height as the player
    enemies = pygame.sprite.Group()
    spawn_delay = 500  # Time in milliseconds between each enemy spawn
    last_spawn_time = pygame.time.get_ticks()  # Track the last spawn time

    running = True
    defeated_enemies = 0  # Counter for defeated enemies
    boss_fight = False  # Flag to start the boss fight
    boss = None  # Boss object
    boss_projectiles = pygame.sprite.Group()

    while running:
        # Clear the screen
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_f:
                    player.shoot()  # Shoot right
                if event.key == pygame.K_g:  # New key for shooting upwards
                    player.shoot_up()  # Call the shoot_up method

        # Player movement
        keys = pygame.key.get_pressed()
        player.speed_x = 0  # Reset speed by default
        if keys[pygame.K_LEFT]:
            player.speed_x = -5
        if keys[pygame.K_RIGHT]:
            player.speed_x = 5

        # Spawn enemies at intervals
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay and len(enemies) < 20:
            # Randomly select an enemy type to spawn
            enemy_type = random.choice([RegularEnemy, FastEnemy, StrongEnemy, AggressiveEnemy])
            enemy = enemy_type(player)  # Pass the player to AggressiveEnemy for tracking
            enemy.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)  # Random spawn position
            enemy.rect.y = player.rect.y  # Set enemy Y position to player's Y position
            enemies.add(enemy)
            all_sprites.add(enemy)
            last_spawn_time = current_time  # Update last spawn time

        # Update all sprites
        all_sprites.update()

        # Check for projectile collisions with enemies
        for projectile in player.projectiles:
            hit_enemies = pygame.sprite.spritecollide(projectile, enemies, True)
            if hit_enemies:
                projectile.kill()  # Destroy the projectile
                defeated_enemies += len(hit_enemies)  # Increment defeated enemies count

        # Check for player collisions with regular enemies
        if pygame.sprite.spritecollide(player, enemies, True):
            player.health -= 10  # Decrease health on collision
            defeated_enemies += 1  # Increment defeated enemies count
            if player.health <= 0:
                game_over()

        # Remove enemies that reach the bottom of the screen
        for enemy in enemies:
            if enemy.rect.y > SCREEN_HEIGHT:
                enemy.kill()  # Remove enemy from all sprites
                defeated_enemies += 1  # Increment defeated enemies count

        # Display player's health
        draw_text(f'Health: {player.health}', font, BLACK, screen, SCREEN_WIDTH - 100, 30)

        # Start boss fight only after all enemies are defeated
        if not enemies and not boss_fight:  # Ensure no remaining enemies
            boss_fight = True
            boss = BossEnemy(boss_projectiles)
            all_sprites.add(boss)

        # Check for player collisions with the boss
        if boss and pygame.sprite.collide_rect(player, boss):
            player.health -= 10  # Decrease player health on boss collision
            if player.health <= 0:
                game_over()

        # Check for projectile collisions with the boss
        if boss:
            for projectile in player.projectiles:
                if pygame.sprite.collide_rect(projectile, boss):
                    projectile.kill()  # Destroy the projectile
                    boss.health -= 10  # Decrease boss health on hit
                    if boss.health <= 0:
                        boss_defeated()

            # Boss attack logic
            for projectile in boss_projectiles:  # Check for each projectile fired by the boss
                if pygame.sprite.collide_rect(player, projectile):  # Check if the player collides with the projectile
                    player.health -= 5  # Decrease player health on collision with projectile
                    projectile.kill()  # Destroy the projectile after collision
                    if player.health <= 0:
                        game_over()

        # Draw the boss health bar if the boss is present
        if boss:
            draw_health_bar(boss, screen)

        # Draw all sprites
        all_sprites.draw(screen)

        # Refresh the display
        pygame.display.flip()
        pygame.time.delay(30)




def level_3():
    screen.fill(WHITE)

    player = Player()  # Create the player instance
    all_sprites.add(player)  # Add the player to the sprite group

    # Create enemies (20 total), ensuring they spawn at the same height as the player
    enemies = pygame.sprite.Group()
    spawn_delay = 500  # Time in milliseconds between each enemy spawn
    last_spawn_time = pygame.time.get_ticks()  # Track the last spawn time

    running = True
    defeated_enemies = 0  # Counter for defeated enemies
    boss_fight = False  # Flag to start the boss fight
    boss = None  # Boss object
    boss_projectiles = pygame.sprite.Group()

    while running:
        # Clear the screen
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_f:
                    player.shoot()  # Shoot right
                if event.key == pygame.K_g:  # New key for shooting upwards
                    player.shoot_up()  # Call the shoot_up method

        # Player movement
        keys = pygame.key.get_pressed()
        player.speed_x = 0  # Reset speed by default
        if keys[pygame.K_LEFT]:
            player.speed_x = -5
        if keys[pygame.K_RIGHT]:
            player.speed_x = 5

        # Spawn enemies at intervals
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay and len(enemies) < 20:
            # Randomly select an enemy type to spawn
            enemy_type = random.choice([RegularEnemy, FastEnemy, StrongEnemy, AggressiveEnemy])
            enemy = enemy_type(player)  # Pass the player to AggressiveEnemy for tracking
            enemy.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)  # Random spawn position
            enemy.rect.y = player.rect.y  # Set enemy Y position to player's Y position
            enemies.add(enemy)
            all_sprites.add(enemy)
            last_spawn_time = current_time  # Update last spawn time

        # Update all sprites
        all_sprites.update()

        # Check for projectile collisions with enemies
        for projectile in player.projectiles:
            hit_enemies = pygame.sprite.spritecollide(projectile, enemies, True)
            if hit_enemies:
                projectile.kill()  # Destroy the projectile
                defeated_enemies += len(hit_enemies)  # Increment defeated enemies count

        # Check for player collisions with regular enemies
        if pygame.sprite.spritecollide(player, enemies, True):
            player.health -= 10  # Decrease health on collision
            defeated_enemies += 1  # Increment defeated enemies count
            if player.health <= 0:
                game_over()

        # Remove enemies that reach the bottom of the screen
        for enemy in enemies:
            if enemy.rect.y > SCREEN_HEIGHT:
                enemy.kill()  # Remove enemy from all sprites
                defeated_enemies += 1  # Increment defeated enemies count

        # Display player's health
        draw_text(f'Health: {player.health}', font, BLACK, screen, SCREEN_WIDTH - 100, 30)

        # Start boss fight only after all enemies are defeated
        if not enemies and not boss_fight:  # Ensure no remaining enemies
            boss_fight = True
            boss = BossEnemy(boss_projectiles)
            all_sprites.add(boss)

        # Check for player collisions with the boss
        if boss and pygame.sprite.collide_rect(player, boss):
            player.health -= 10  # Decrease player health on boss collision
            if player.health <= 0:
                game_over()

        # Check for projectile collisions with the boss
        if boss:
            for projectile in player.projectiles:
                if pygame.sprite.collide_rect(projectile, boss):
                    projectile.kill()  # Destroy the projectile
                    boss.health -= 10  # Decrease boss health on hit
                    if boss.health <= 0:
                        boss_defeated()

            # Boss attack logic
            for projectile in boss_projectiles:  # Check for each projectile fired by the boss
                if pygame.sprite.collide_rect(player, projectile):  # Check if the player collides with the projectile
                    player.health -= 5  # Decrease player health on collision with projectile
                    projectile.kill()  # Destroy the projectile after collision
                    if player.health <= 0:
                        game_over()

        # Draw the boss health bar if the boss is present
        if boss:
            draw_health_bar(boss, screen)

        # Draw all sprites
        all_sprites.draw(screen)

        # Refresh the display
        pygame.display.flip()
        pygame.time.delay(30)




def level_3():
    screen.fill(WHITE)

    player = Player()  # Create the player instance
    all_sprites.add(player)  # Add the player to the sprite group

    # Create enemies (30 total), ensuring they spawn at the same height as the player
    enemies = pygame.sprite.Group()
    spawn_delay = 500  # Time in milliseconds between each enemy spawn
    last_spawn_time = pygame.time.get_ticks()  # Track the last spawn time

    running = True
    defeated_enemies = 0  # Counter for defeated enemies
    boss_fight = False  # Flag to start the boss fight
    boss = None  # Boss object
    boss_projectiles = pygame.sprite.Group()

    while running:
        # Clear the screen
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_f:
                    player.shoot()  # Shoot right
                if event.key == pygame.K_g:  # New key for shooting upwards
                    player.shoot_up()  # Call the shoot_up method

        # Player movement
        keys = pygame.key.get_pressed()
        player.speed_x = 0  # Reset speed by default
        if keys[pygame.K_LEFT]:
            player.speed_x = -5
        if keys[pygame.K_RIGHT]:
            player.speed_x = 5

        # Spawn enemies at intervals
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay and len(enemies) < 30:  # Spawn up to 30 enemies
            # Randomly select an enemy type to spawn
            enemy_type = random.choice([RegularEnemy, FastEnemy, StrongEnemy, AggressiveEnemy])
            enemy = enemy_type(player)  # Pass the player to AggressiveEnemy for tracking
            enemy.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)  # Random spawn position
            enemy.rect.y = player.rect.y  # Set enemy Y position to player's Y position
            enemies.add(enemy)
            all_sprites.add(enemy)
            last_spawn_time = current_time  # Update last spawn time

        # Update all sprites
        all_sprites.update()

        # Check for projectile collisions with enemies
        for projectile in player.projectiles:
            hit_enemies = pygame.sprite.spritecollide(projectile, enemies, True)
            if hit_enemies:
                projectile.kill()  # Destroy the projectile
                defeated_enemies += len(hit_enemies)  # Increment defeated enemies count

        # Check for player collisions with regular enemies
        if pygame.sprite.spritecollide(player, enemies, True):
            player.health -= 10  # Decrease health on collision
            defeated_enemies += 1  # Increment defeated enemies count
            if player.health <= 0:
                game_over()

        # Remove enemies that reach the bottom of the screen
        for enemy in enemies:
            if enemy.rect.y > SCREEN_HEIGHT:
                enemy.kill()  # Remove enemy from all sprites
                defeated_enemies += 1  # Increment defeated enemies count

        # Display player's health
        draw_text(f'Health: {player.health}', font, BLACK, screen, SCREEN_WIDTH - 100, 30)

        # Start boss fight only after all enemies are defeated
        if not enemies and not boss_fight:  # Ensure no remaining enemies
            boss_fight = True
            boss = BossEnemy(boss_projectiles)
            all_sprites.add(boss)

        # Check for player collisions with the boss
        if boss and pygame.sprite.collide_rect(player, boss):
            player.health -= 10  # Decrease player health on boss collision
            if player.health <= 0:
                game_over()

        # Check for projectile collisions with the boss
        if boss:
            for projectile in player.projectiles:
                if pygame.sprite.collide_rect(projectile, boss):
                    projectile.kill()  # Destroy the projectile
                    boss.health -= 10  # Decrease boss health on hit
                    if boss.health <= 0:
                        boss_defeated()

            # Boss attack logic
            for projectile in boss_projectiles:  # Check for each projectile fired by the boss
                if pygame.sprite.collide_rect(player, projectile):  # Check if the player collides with the projectile
                    player.health -= 5  # Decrease player health on collision with projectile
                    projectile.kill()  # Destroy the projectile after collision
                    if player.health <= 0:
                        game_over()

        # Draw the boss health bar if the boss is present
        if boss:
            draw_health_bar(boss, screen)

        # Draw all sprites
        all_sprites.draw(screen)

        # Refresh the display
        pygame.display.flip()
        pygame.time.delay(30)








def game_over():
    """Handles the game over state."""
    all_sprites.empty()  # Clear all sprites from the screen
    draw_text("You Died!", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20)
    draw_text("Game Over!", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20)
    pygame.display.flip()
    pygame.time.delay(2000)  # Delay for 2 seconds for the player to see the message
    screen.fill(WHITE)  # Fill the screen with white
    game_menu()  # Return to the game menu

def boss_defeated():
    """Handles the state when the boss is defeated."""
    all_sprites.empty()  # Clear all sprites from the screen
    draw_text("Boss Defeated!", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20)
    pygame.display.flip()
    pygame.time.delay(3000)  # Delay for 2 seconds for the player to see the message
    screen.fill(WHITE)  # Fill the screen with white
    game_menu()  # Return to the game menu


# Main game loop
def game_menu():
    # Create a player instance
    player = Player()
    all_sprites.add(player)

    running = True
    while running:
        screen.fill(WHITE)

        # Display the menu options with centered text
        draw_text("2D Game Menu", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        draw_text("Press 1 for Level 1", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        draw_text("Press 2 for Level 2", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5)
        draw_text("Press 3 for Level 3", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.35)
        draw_text("Press Q to Exit", font, BLACK, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2)

        # Update projectiles
        player.projectiles.update()

        # Draw the player and projectiles
        all_sprites.draw(screen)
        player.projectiles.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Break out of the loop and quit gracefully
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    all_sprites.empty()  # Clear all sprites before starting a new level
                    level_1()  # Start level 1
                elif event.key == pygame.K_2:
                    all_sprites.empty()  # Clear all sprites before starting a new level
                    level_2()  # Start level 2
                elif event.key == pygame.K_3:
                    all_sprites.empty()  # Clear all sprites before starting a new level
                    level_3()  # Start level 3
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False  # Exit the game
                elif event.key == pygame.K_f:  # Shoot horizontally
                    player.shoot()  # Shoot when 'F' is pressed
                elif event.key == pygame.K_g:  # Shoot vertically
                    player.shoot_up()  # Shoot vertically when 'G' is pressed

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # Quit the game properly
    pygame.quit()
    sys.exit()


# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
boss_projectiles = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

# Run the main menu
game_menu()
