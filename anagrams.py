a,b= input('anagrams\nEnter first & second string: ').split(' ')
if (sorted(a) == sorted(b)):
    print('strings are anagrams')
else:
    print('strings not a anagrams')
 