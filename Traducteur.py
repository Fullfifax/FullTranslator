from googletrans import Translator, LANGUAGES

class Traduction():
	def __init__(self):
		self.languageList = list(LANGUAGES.values())
	def translation(self, txt="Type here", src = LANGUAGES.values(), dest = LANGUAGES.values()):
		self.traduire  = Translator()
		self.txt = txt
		self.src = src
		self.dest = dest
		try:
			self.translated = self.traduire.translate(self.txt, src = self.src, dest = self.dest)
		except:
			self.translated = self.traduire.translate(self.txt)
		self.text = self.translated.text
		return self.text





