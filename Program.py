from urllib.request import Request, urlopen


def read_text(file):
	archive = open(file)
	text = archive.read()
	check_profanity(text)
	archive.close()

def check_profanity(text_to_check):
	q = Request("http://www.wdylike.appspot.com/?q=" + text_to_check)
	q.add_header('User-Agent', 'Mozilla/5.0')
	connection = urlopen(q)
	output = connection.read()
	connection.close()
	print(output)

file= r"C:\Users\Cincinnatus\repositorios\lector\text.txt"
read_text(file)