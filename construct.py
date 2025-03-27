def grab(filename):
	returnString = ""
	with open(filename, "r+") as file:
		for line in file.readlines():
			returnString += "\t"
			returnString += line

	return returnString

def start(file):
	file.write("""<!doctype html>
<html>
<head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
""")

def middle(file):
	file.write("""</head>
<body>
""")
	
def end(file):
	file.write("""<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")


with open("index.html", "w+") as file:
	start(file)
	##############
	# header stuff
	##############
	middle(file)
	############
	# body stuff
	############
	file.write(grab("components/navbar"))
	file.write(grab("components/1stRow"))

	file.write(grab("components/footer"))
	end(file)
