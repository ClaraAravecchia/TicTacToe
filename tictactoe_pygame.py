# -*- coding: utf-8 -*-
import sys, pygame, random, time
from pygame.locals import *


def draw_table(screen):
	"""
	Desenha as linhas iniciais
	"""
	screen.fill(color_screen)
	
    # Vertical Lines
	pygame.draw.line(screen, color_line, ( S_1, 15),  ( S_1, S ))
	pygame.draw.line(screen, color_line, ( S_2, 15),  ( S_2, S ))

    #Horizontal Lines
	pygame.draw.line(screen, color_line, ( 15, S_1),   ( S, S_1 ))
	pygame.draw.line(screen, color_line, ( 15, S_2),   ( S, S_2 ))
	

def verify_sqr(x, y):
	"""
	Transforma uma posicao cartesiana em um numero de quadradinho escolhido pelo player X
	"""
	if (x < S_1 and y < S_1): return verify_taken(1, 'x')
	if (x < S_2 and y < S_1 and x > S_1): return verify_taken(2, 'x')
	if (x > S_2 and y < S_1): return verify_taken(3, 'x')

	if (x < S_1 and y < S_2 and y > S_1): return verify_taken(4, 'x')
	if (x < S_2 and y < S_2 and y > S_1 and x > S_1): return verify_taken(5, 'x')
	if (x > S_2 and y < S_2 and y > S_1): return verify_taken(6, 'x')

	if (x < S_1 and y > S_2): return verify_taken(7, 'x')
	if (x < S_2 and y > S_2 and x > S_1): return verify_taken(8, 'x')
	if (x > S_2 and y > S_2): return verify_taken(9, 'x')

	
def draw_X(sqr):
	"""
	Desenha X
	"""
	#print("X - %i" %sqr) 
	p0 = 50
	p1 = S_1 - p0
	p2 = S_2 - p0

	p3 = S_1 + p0
	p4 = S_2 + p0
	p5 = size - p0
	
	if sqr == 1:
		pygame.draw.line(screen, color_line, (p0, p0), (p1, p1), 8)
		pygame.draw.line(screen, color_line, (p0, p1), (p1, p0), 8)

	elif sqr == 2:
		pygame.draw.line(screen, color_line, (p3, p0), (p2, p1), 8)
		pygame.draw.line(screen, color_line, (p3, p1), (p2, p0), 8)
	
	elif sqr == 3:
		pygame.draw.line(screen, color_line, (p4, p0), (p5, p1), 8)
		pygame.draw.line(screen, color_line, (p4, p1), (p5, p0), 8)
	
	elif sqr == 4:
		pygame.draw.line(screen, color_line, (p0, p2), (p1, p3), 8)
		pygame.draw.line(screen, color_line, (p0, p3), (p1, p2), 8)

	elif sqr == 5:
		pygame.draw.line(screen, color_line, (p3, p3), (p2, p2), 8)
		pygame.draw.line(screen, color_line, (p3, p2), (p2, p3), 8)

	elif sqr == 6:
		pygame.draw.line(screen, color_line, (p4, p3), (p5, p2), 8)
		pygame.draw.line(screen, color_line, (p4, p2), (p5, p3), 8)

	elif  sqr == 7:
		pygame.draw.line(screen, color_line, (p0, p4), (p1, p5), 8)
		pygame.draw.line(screen, color_line, (p0, p5), (p1, p4), 8)

	elif sqr == 8:
		pygame.draw.line(screen, color_line, (p3, p4), (p2, p5), 8)
		pygame.draw.line(screen, color_line, (p3, p5), (p2, p4), 8)
		
	else:
		pygame.draw.line(screen, color_line, (p4, p5), (p5, p4), 8)
		pygame.draw.line(screen, color_line, (p4, p4), (p5, p5), 8)

def draw_O():
	"""
	Escolhe e desenha O
	"""
	pos = random.choice(range(1, 10))
	
	while not verify_taken(pos, 'o'):
		pos = random.choice(range(1, 10))
	p1 = S_1 - 100
	p2 = S_2 - 100
	p3 = S_2 + 100
	#print ("O -  ", pos)


	if pos == 1:
		pygame.draw.circle(screen, color_line, (p1, p1), 50, 8) 
	elif pos == 2:
		pygame.draw.circle(screen, color_line, (p2, p1), 50, 8)
	elif pos == 3:
		pygame.draw.circle(screen, color_line, (p3, p1), 50, 8)
	elif pos == 4:
		pygame.draw.circle(screen, color_line, (p1, p2), 50, 8)
	elif pos == 5:
		pygame.draw.circle(screen, color_line, (p2, p2), 50, 8)
	elif pos== 6:
		pygame.draw.circle(screen, color_line, (p3, p2), 50, 8)
	elif pos == 7:
		pygame.draw.circle(screen, color_line, (p1, p3), 50, 8)
	elif pos == 8:
		pygame.draw.circle(screen, color_line, (p2, p3), 50, 8)
	else:
		pygame.draw.circle(screen, color_line, (p3, p3), 50, 8)


def verify_taken(sqr, player):
	"""
	Verifica se o quadradinho ja foi escolhido.
	Se não foi, associa o quadradinho ao player que o escolheu.
	"""
	if not sqr in taken_list:
		taken_list.append(sqr) 
		played[sqr] = player
		return sqr
	elif sqr in taken_list and game == True:
		#print(" %i Already choosen!" %sqr)
		return None
			


def verify_winner():
	"""
	Verifica se alguem ganhou
	"""
	pygame.display.update()
	if played[1] == played[5] == played[9] and played[9] != None: return win_looseMsg(played[1])
	if played[3] == played[5] == played[7] and played[7] != None: return win_looseMsg(played[3])
	if played[1] == played[2] == played[3] and played[2] != None: return win_looseMsg(played[1])
	if played[4] == played[5] == played[6] and played[6] != None: return win_looseMsg(played[4])
	if played[7] == played[8] == played[9] and played[9] != None: return win_looseMsg(played[7])
	if played[1] == played[4] == played[7] and played[7] != None: return win_looseMsg(played[1])
	if played[2] == played[5] == played[8] and played[8] != None: return win_looseMsg(played[2])
	if played[3] == played[6] == played[9] and played[9] != None: return win_looseMsg(played[3])
	if not None in played.values(): return win_looseMsg(None)


def win_looseMsg(winner):
	"""
	Imprime a mensagem de quem ganhou
	"""
	time.sleep(2)
	screen.fill(color_screen)
	pygame.font.init()

	pygame.display.flip()
	m_font = pygame.font.SysFont("Comic Sans MS", 60)
	position = (size/4, size/2)

	if winner == 'x':
		text = m_font.render("Você Ganhou!!", False, color_line)
	elif winner == 'o':
		text = m_font.render("Você Perdeu.", False, color_line)
	else:
		text = m_font.render("Empate.", False, color_line)
	screen.blit(text, (position))
	pygame.display.update()
	time.sleep(2)
	pygame.font.quit()
	return True	


def new_game():
	"""
	Inicializa o jogo
	"""


	screen = pygame.display.set_mode(( size, size ))
	screen.fill(color_screen)
	pygame.display.set_caption("Tic Tac Toe")
	draw_table(screen)
	
	global taken_list, played
	taken_list = []
	played = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8:None, 9: None}

	
def main():
	while True:
		global game
		game = True
		new_game()
		while None in played.values() and game == True:
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit(0)
					return
				elif event.type == MOUSEBUTTONUP:
					not_chosen = verify_sqr(event.pos[0], event.pos[1]) # marca o quadrado na pos correta e retorna o quadrado escolhido
					if not_chosen:
						draw_X(not_chosen)
						if verify_winner(): game = False 
						else: draw_O()
					if verify_winner(): game = False
					#print(played)
					#print(taken_list)

			pygame.display.update()
			
size = 600
S = size - 15

color_screen = (49, 10, 100)
color_line = (255, 255, 255)

S_1 = int(S*(1/3.0)) #200
S_2 = int(S*(2/3.0)) #400

screen = pygame.display.set_mode(( size, size ))
main()