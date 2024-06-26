import pygame
import random
import os
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("recursos/icone.jfif")
personagemPrincipal = pygame.image.load("recursos/personagemPrincipal.png")
fundo = pygame.image.load("recursos/fundo.png")
fundoStart = pygame.image.load("recursos/fundoStart.png")
fundoDead = pygame.image.load("recursos/fundoDead.png")

praca = pygame.image.load("recursos/praca.jpg")
praca = pygame.transform.scale(praca, (100, 75))
skol = pygame.image.load("recursos/inimigo.png")
brahma = pygame.image.load("recursos/inimigo2.png")
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Show de Bola - The Game")
pygame.display.set_icon(icone)
#missileSound = pygame.mixer.Sound("assets/missile.wav")
#explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonteMorte = pygame.font.SysFont("arial",120)
#pygame.mixer.music.load("assets/ironsound.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )
amarelo = (255, 255, 0)


def jogar(nome):
    #pygame.mixer.Sound.play(missileSound)
    #pygame.mixer.music.play(-1)
    posicaoXPersona = 400
    posicaoYPersona = 300
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    posicaoXMissel = 400
    posicaoYMissel = -240
    velocidadeMissel = 1
    posicaoXMisselb = 300
    posicaoYMisselb = -240
    velocidadeMisselb = 1
    pontos = 0
    larguraPersona = 150
    alturaPersona = 214
    larguaMissel  = 60
    alturaMissel  = 120
    larguaMisselb  = 60
    alturaMisselb  = 120
    dificuldade  = 30
    aumentando = True
    radius = 20

    posicaoXpraca = random.randint(0, tamanho[0] - 50)
    posicaoYpraca = random.randint(0, tamanho[0] - 50)
    movimentoXpraca= random.choice([-1,1])
    movimentoYpraca= random.choice([-1,1])
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
                
        posicaoXPersona = posicaoXPersona + movimentoXPersona            
        posicaoYPersona = posicaoYPersona + movimentoYPersona            
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona >550:
            posicaoXPersona = 540
            
        if posicaoYPersona < 0 :
            posicaoYPersona = 10
        elif posicaoYPersona > 473:
            posicaoYPersona = 463
        
            
        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( personagemPrincipal, (posicaoXPersona, posicaoYPersona))
        
        posicaoYMissel = posicaoYMissel + velocidadeMissel
        if posicaoYMissel > 600:
            posicaoYMissel = -240
            pontos = pontos + 1
            velocidadeMissel = velocidadeMissel + 1
            posicaoXMissel = random.randint(0,800)
            
        tela.blit( skol, (posicaoXMissel, posicaoYMissel) ) 
            
        
        posicaoYMisselb = posicaoYMisselb + velocidadeMisselb
        if posicaoYMisselb > 600:
            posicaoYMisselb = -240
            pontos = pontos + 1
            velocidadeMisselb = velocidadeMisselb + 1
            posicaoXMissel = random.randint(0,800)
            #pygame.mixer.Sound.play(missileSound)
            
        tela.blit( brahma, (posicaoXMisselb, posicaoYMisselb) )
        
        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
        pixelsMisselX = list(range(posicaoXMissel, posicaoXMissel + larguaMissel))
        pixelsMisselY = list(range(posicaoYMissel, posicaoYMissel + alturaMissel))
        pixelsMisselXb = list(range(posicaoXMisselb, posicaoXMisselb + larguaMisselb))
        pixelsMisselYb = list(range(posicaoYMisselb, posicaoYMisselb + alturaMisselb))
        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        
        if  len( list( set(pixelsMisselY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        
        if  len( list( set(pixelsMisselYb).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsMisselXb).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)

        posicaoYpraca += movimentoYpraca
        posicaoXpraca += movimentoXpraca
        if posicaoXpraca <= 0 or posicaoXpraca >= tamanho[0] - 50:
         movimentoXpraca = - movimentoXpraca
                
        if posicaoYpraca <= 0 or posicaoYpraca >= tamanho[1] - 50:
         movimentoYpraca = - movimentoYpraca

        tela.blit(praca, (posicaoXpraca, posicaoYpraca))


        pygame.draw.circle(tela, amarelo, (750, 50), radius)
        if aumentando:
          radius += 0.15
          if radius >=40:
             aumentando = False
        else:
          radius -=0.15
          if radius <=10:
           aumentando = True        
        
        pygame.display.update()
        relogio.tick(60)

#joia
def dead(nome, pontos):
    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(explosaoSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("Show de Bola","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,50))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (330,482))

        
        
        pygame.display.update()
        relogio.tick(60)

start()