"""
jeoparpy.ui

DESCRIPTION:
  This package contains all the game presentation logic. All creating, 
  updating, and drawing of pygame.Surfaces, as well as blitting surfaces 
  to the screen, is done in this package.
  
USAGE:
  During primary gameplay, main should directly interact with only a single 
  instance of the Controller class (see controller.py).
  
  Special sequences have do_* functions (see below) that main also may call
  outside of the main game loop.
  
CUSTOMIZATION:
  See instructions in config.py and resmaps.py.
"""
from jeoparpy.ui.categoryscroll import do_scroll
from jeoparpy.ui.congrats import do_congrats
from jeoparpy.ui.controller import Controller
from jeoparpy.ui.credits import do_credits
from jeoparpy.ui.intro import do_intro
