vowels=['a','e','i','o','u']
words=input("Please enter the words here: ")

found={}

for i in vowels:
    found[i]=0
	
for letter in words:
    if letter in vowels:
	    found[letter] += 1

for k,v in sorted(found.items()):
    print(k, 'appears', v, 'times.' )