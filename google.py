from re import A
import googletrans
from googletrans import Translator
#print(googletrans.LANGUAGES)
t = Translator()
ab = t.translate("em dep qua", src="vi", dest="en")
print(ab.text)