from googletrans import Translator

translator = Translator()
til = input("tilni kiriting: ")
text = input("so'zni kiriting: ")
tarjima = translator.translate(text, dest = til)

print("Natija:", tarjima.text)

#_______________________________________
#| from googletrans import Translator   |
#| translator = Translator(setattr)     |
#|print("1. O'zbek tili")               |
#|print("2. Ingliz tili")               |
#| print("2. Turk tili")                |
#|______________________________________|
