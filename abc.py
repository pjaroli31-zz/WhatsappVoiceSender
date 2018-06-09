import speech_recognition as sr
from whatsapp_send import sender

def record():
	r = sr.Recognizer()
	#r.energy_threshold = 500
	with sr.Microphone() as source:
		print('say something.......')
		audio = r.listen(source)


	print('do you want to send this message:SAY-->(Yes/No) ' +r.recognize_google(audio))
	with sr.Microphone() as source:
		ans = r.listen(source)
	print(r.recognize_google(ans).upper())
	if r.recognize_google(ans).upper() == "YES" :
		sender(r.recognize_google(audio))
	else:
		record()	

record()		