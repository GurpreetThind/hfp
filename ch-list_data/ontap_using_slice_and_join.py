phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)

new_phrase=''.join(plist[1:3])+''.join(plist[-7:-9:-1])+''.join(plist[-5:-7:-1])
print(plist)
print(new_phrase)
