def read_text(file):
	archive = open(file)
	text = archive.read()
	print(text)
	archive.close()

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()
	print(output)
	
file= r"C:\Users\Cincinnatus\repositorios\lector\text.txt"
read_text(file)