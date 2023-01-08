favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name,language in favourite_languages.items():
	print(name.title() + "'s favourite language is " + 
		language.title() + ".")

investigate_persons = ["jen","sarah","phil","tom"]
for p in investigate_persons:
	if p in favourite_languages.keys():
		print("Thanks")
	else:
		print("Please take our phll!")
