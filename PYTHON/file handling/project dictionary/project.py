import json
import difflib
from difflib import get_close_matches

with open("data.json", "r") as file:
	data = file.read()
	words = json.loads(data)

def closeMatch(word):
	try:
		word = get_close_matches(word, words.keys())[0]
		print("Do you mean: %s"%(word))
		choice = input()
		if choice == "yes":
			print(words[word][0])
		else:
			print("Word not found")
	except:
		print("Invalid Word")

def translate(word):
	word = word.lower()
	if word in words:
		print(words[word][0])
	else:
		closeMatch(word)

print("Enter word to search: ", end = "")
word = input()
translate(word)
