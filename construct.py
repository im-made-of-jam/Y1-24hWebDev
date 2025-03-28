def grab(filename):
	returnString = f"	<!-- {filename} -->\n"
	hadLines = False
	with open(filename, "r+") as file:
		for line in file.readlines():
			hadLines = True
			returnString += "\t"
			returnString += line

	returnString += f"	<!-- end {filename} -->\n"

	return returnString if hadLines else ""

def start(file):
	file.write("""<!doctype html>
<html lang="en">
<head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
	<title>The Company Company</title>
""")

def middle(file):
	file.write("""</head>
<body class="bg-dark">
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
	file.write(grab("components/header"))
	middle(file)
	############
	# body stuff
	############
	file.write(grab("components/navbar"))
	file.write(grab("components/1stRow"))
	file.write(grab("components/2ndRow"))
	file.write(grab("components/3rdRow"))

	file.write(grab("components/footer"))

	#########################
	# end of the file
	# write nothing new below
	#########################
	end(file)
