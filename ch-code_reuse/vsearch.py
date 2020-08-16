def searchforvowels():
	vowels=set('aeiou')
	word=input("Please enter the string you would like to inspect: ")
	found=vowels.intersection(set(word))
	for char in found:
		print(char)
		
		
searchforvowels()