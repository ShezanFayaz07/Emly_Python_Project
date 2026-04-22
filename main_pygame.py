import pygame
pygame.init()

WIN =  pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Hangman Game")

clock = pygame.time.Clock()

game_state = "menu"

font_big = pygame.font.SysFont('Arial', 80)
font_medium = pygame.font.SysFont('Arial', 46)
font_small = pygame.font.SysFont('Arial', 34)


selected_word = ''
attempts_left = 0
guessed_letters = set()

WordsList = ["apple", "banana", "grapes", "orange", "mango"]

selected_word = ''
User_Guess = ''

Wrong_letters = set()

def draw_menu():
    WIN.fill((30, 30, 30))

    title   = font_big.render("HANGMAN", True, (255, 215, 0))
    welcome = font_medium.render("Welcome to the Game!", True, (255, 255, 255))
    prompt  = font_small.render("Press Y to Start or N to Quit", True, (180, 180, 180))

    WIN.blit(title,   (1200//2 - title.get_width()//2,   200))  
    WIN.blit(welcome, (1200//2 - welcome.get_width()//2, 300)) 
    WIN.blit(prompt,  (1200//2 - prompt.get_width()//2,  380)) 

def draw_rules():
    WIN.fill((30,30,30))

    title = font_big.render("HANGMAN", True, (255, 215, 0))
    rules = [
        "Rules:",
        "1. Enter only one letter (a-z) each turn.",
        "2. Correct letter -> revealed in all positions.",
        "3. Wrong letter -> attempts decrease by 1.",
        "4. Repeated guess -> warning, no attempt loss.",
        "5. You win if all letters are revealed.",
        "6. You lose if attempts reach 0."
    ]

    WIN.blit(title, (1200//2 - title.get_width()//2, 50))
    for i in rules:
        rule_text = font_small.render(i, True, (255, 255, 255))
        WIN.blit(rule_text, (1200//2 - rule_text.get_width()//2, 150 + rules.index(i) * 50 ))


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if game_state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_state = "rules"
                elif event.key == pygame.K_n:
                    running = False

    if game_state == "menu":
        draw_menu()
    elif game_state == "rules":
        draw_rules()
    pygame.display.update()
pygame.quit()
