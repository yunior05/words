def read_text(file):
	archive = open(file)
	text = archive.read()
	print(text)
	archive.close()


file= r"C:\Users\Cincinnatus\repositorios\lector\text.txt"
read_text(file)