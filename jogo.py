import random
import pygame

pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Popeye faminto!")
altura = 703
largura = 626
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
preto = (0, 0, 0)

fundo = pygame.image.load("assets/backgroundok.jpg")
popeye = pygame.image.load("assets/jogadorok.png")
spinach = pygame.image.load("assets/spinach.png")
badSpinach = pygame.image.load("assets/badspinach.png")

popeye = pygame.transform.scale(popeye, (185, 160))
spinach = pygame.transform.scale(spinach, (72, 72))
badSpinach = pygame.transform.scale(badSpinach, (72, 72))

def escreverTexto(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 15)
    textoDisplay = fonte.render(texto, True, preto)
    gameDisplay.blit(textoDisplay, (510, 30))
    pygameDisplay.update()

def morreu():
    fonte = pygame.font.Font("freesansbold.ttf", 35)
    fonte2 = pygame.font.Font("freesansbold.ttf", 25)
    textoDisplay = fonte.render("Você deixou o Popeye morrer!", True, preto)
    textoDisplay2 = fonte2.render("aperte enter para jogar novamente!", True, preto)
    gameDisplay.blit(textoDisplay, (70, 388))
    gameDisplay.blit(textoDisplay2, (110, 430))
    pygameDisplay.update()

def jogar():
    jogando = True
    popeyeX = 140 
    popeyeY = 500
    movimentoPopeyeX = 0
    larguraPopeye = 77
    alturaPopeye = 110

    alturaBadSpinach = 70
    larguraBadSpinach = 50
    posicaoBadSpinachX = 400
    posicaoBadSpinachY = -240
    velocidadeBadSpinach = 5

    spinachY = -100
    spinachX = 300
    larguraSpinach = 30
    alturaSpinach = 50
    velocidadeSpinach = 5

    pontos = 0
        
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoPopeyeX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoPopeyeX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoPopeyeX = 0
            
        if jogando:
            if posicaoBadSpinachY > altura:
                posicaoBadSpinachY = -240
                posicaoBadSpinachX = random.randint(0,largura)
                velocidadeBadSpinach = velocidadeBadSpinach + 1
                # pontos = pontos + 1
                   
            else:
                posicaoBadSpinachY = posicaoBadSpinachY + velocidadeBadSpinach

        if jogando:
            if spinachY > altura:
                spinachY = -240
                spinachX = random.randint(0,largura)
                velocidadeSpinach = velocidadeSpinach 
                # pontos = pontos + 1
            else:
                spinachY = spinachY + velocidadeSpinach

            if popeyeX + movimentoPopeyeX >0 and popeyeX + movimentoPopeyeX < largura - larguraPopeye:
                popeyeX = popeyeX + movimentoPopeyeX
            gameDisplay.fill(preto)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(popeye, (popeyeX, popeyeY))
            gameDisplay.blit(badSpinach, (posicaoBadSpinachX, posicaoBadSpinachY))
            gameDisplay.blit(spinach, (spinachX, spinachY))

            pixelsXpopeye = list(range(popeyeX, popeyeX+larguraPopeye))
            pixelsYpopeye = list(range(popeyeY, popeyeY+alturaPopeye))

            pixelXbadSpinach = list(range(posicaoBadSpinachX, posicaoBadSpinachX + larguraBadSpinach))
            pixelYbadSpinach = list(range(posicaoBadSpinachY, posicaoBadSpinachY + alturaBadSpinach))

            colisaoY = len(list(set(pixelYbadSpinach) & set(pixelsYpopeye) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXbadSpinach) & set(pixelsXpopeye) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando = False

            pixelXspinach = list(range(spinachX, spinachX + larguraSpinach))
            pixelYspinach = list(range(spinachY, spinachY + alturaSpinach))

            coletaS = len(list(set(pixelYspinach)& set(pixelsYpopeye)))
            if coletaS > 0:
                coletaXS = len(list(set(pixelXspinach) & set (pixelsXpopeye)))
                print (coletaXS)
                if coletaXS >= 30:
                    pontos = pontos + 1
                    spinachY = -150

        escreverTexto("Pontos: "+str(pontos))
                   
        pygameDisplay.update()
        clock.tick(60)

jogar()