# Compile this file if you want to convert these files to .exe

import cx_Freeze
import sys

base = None

if sys.platform == "win32":
	base = "Win32GUI"
else:
	base = "Win64GUI"

executables = [cx_Freeze.Executable("Translator.py", base=base, icon = "icon.ico")]

cx_Freeze.setup(
	name = "Fulltranslator reflect v1.0",
	options = {"build_exe" : {"packages" : ["tkinter", "googletrans"], 
							  "include_files" : ["icon.ico", "traducteur.py"]}},
	version = "0.01",
	description  = "Fulltranslator reflect est un logiciel de traduction automatique",
	executables = executables
	)
