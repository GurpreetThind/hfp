paranoid_android = "marvin"
# for sting 
for i in paranoid_android:
    print("\t", i)
print('\t')

print(paranoid_android)
# for list of character objects
phrase=list(paranoid_android)
for ch in phrase:
    print("\t",ch)


print(phrase)



#for list to iterate over slice

paranoid_android="Marvin, the Android Marvel of the Universe"

slice_letter=list(paranoid_android)

print(slice_letter)

for i in slice_letter[:7:1]:
    print('\t', i)

for ch in slice_letter[7::3]:
    print('\t'*2, ch)

for char in slice_letter[::-1]:
    print('\t'*3,char)
