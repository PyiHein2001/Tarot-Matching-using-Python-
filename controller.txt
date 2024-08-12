from view import *
import view as vw

class Controller:
	def __init__(*args,**kwargs):
		pass
	
	def _exit():
		answer = vw.askyesno(title="Exit",message="are you sure?")
		if answer:
			return True
		else:
			return False