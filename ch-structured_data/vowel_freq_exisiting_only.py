vowels=['a','e','i','o','u']
phrase=input("Please enter your phrase here: ")

found={}

for letter in phrase:
    if letter in vowels:
	    found.setdefault(letter,0)
	    found[letter] += 1
		
for k,v in sorted(found.items()):
    print(k, 'has appeared', v, 'times in', phrase, '!')
