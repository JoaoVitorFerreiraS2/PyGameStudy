import pygame

# Inicializar o módulo do Pygame


pygame.init()

# Definindo tamanho da janela

X_SIZE = 576
Y_SIZE = 324

window = pygame.display.set_mode(size=(X_SIZE,Y_SIZE))

# Carregar imagem e gerar uma superficie
# = convert.alpha serve para otimizar
bg_fundo = pygame.image.load('./asset/city.png').convert_alpha()
player1_ship = pygame.image.load('./asset/ship.png').convert_alpha()

# Obter o retangulo da superficie

bg_rect = bg_fundo.get_rect(left=0, top=0)  
player1_rect = player1_ship.get_rect(left=100, top=100)  

# Desenha na janela
window.blit(source=bg_fundo, dest=bg_rect)
window.blit(source=player1_ship, dest=player1_rect)

#atualizar a janela
pygame.display.flip()

# Colocar um relógio no nosso jogo

clock = pygame.time.Clock()

# Carrega Som 

pygame.mixer_music.load('./asset/fase1.mp3')
pygame.mixer_music.set_volume(0.1)
pygame.mixer.music.play() 


while True:
    clock.tick(100) # Esse loop está acontecendo x vezes por segundo
    print(f'FPS: {clock.get_fps():.0f}')

    window.blit(source=bg_fundo, dest=bg_rect)
    window.blit(source=player1_ship, dest=player1_rect)
    pygame.display.flip()

    # Nesse for estou pegando qualquer evento que acontecer na tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        player1_rect.centery += 1

    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        player1_rect.centery -= 1

    if pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]:
        player1_rect.centerx += 1

    if pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
        