from browsercontrol import BrowserControl
from play2048 import play2048
	

browserctl = BrowserControl()
play2048 = play2048(browserctl)

play2048.play()

print ("Total moves: %s" % play2048.move_count)
	


