import pygame

# --- Dimensiones de ventana ---
WIDTH = 800
HEIGHT = 800

# --- Colores ---

BLACK					=			(  0,   0,   0)
DARK_BLUE				=			(  0,   0, 100)
BLUE					=			(  0,   0, 255)
DARK_GREEN			    =			(  0, 100,   0)
GREENISH_BLUE			=			(  0, 100, 100)
LIGHT_TURQUOISE		    =			(  0, 100, 255)
GREEN					=			(  0, 255,   0)
WATERY_GREEN			=			(  0, 255, 100)
CYAN					=			(  0, 255, 255)

RED						=			(255,   0,   0)
DARK_PINK				=			(255,   0, 100)
PINK					=			(255,   0, 255)
ORANGE			   	    =			(255, 100,   0)
RED_PINK				=			(255, 100, 100)
MAGENT				    =			(255, 100, 255)
YELLOW					=			(255, 255,   0)
LIGHT_YELLOW			=			(255, 255, 100)
WHITE					=			(255, 255, 255)

REDDISH_BROWN		    =			(100,   0,   0)
PURPLE					=			(100,   0, 100)
MUSTARD				    =			(100,   0, 255)
GREENISH_BROWN		    =			(100, 100,   0)
GREY					=			(100, 100, 100)
TURQUOISE				=			(100, 100, 255)

PLAYER_SIZE = (30, 30)

#Tamaño Meteoritos

METEOR_SIZE = {
    "grande": (120, 120),
    "mediano": (90, 90),
    "pequeño": (60, 60)
}

#Tiempo de disparo
SHOOT_DELAY = 250
