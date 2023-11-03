print("-----WHALE-TALK TRANSLATOR-----")
print('Enter your message:')
import time
words = str(input())
vowels = ['a', 'e', 'i', 'o', 'u']
resultsArray = []

for i in range(len(words)):
    if words[i] == 'e':
        resultsArray.append(words[i])
    elif words[i] == 'u':
        resultsArray.append(words[i])
    for j in vowels:
        if words[i] == j:
            resultsArray.append(words[i])


whaleSentence = "".join(resultsArray).upper()
time.sleep(1)
print('Translating...')
time.sleep(3)
print('Whale message:')
time.sleep(1)
print(whaleSentence)
time.sleep(1)

print("""/
      .
       ":"
     ___:____     |"\/"|
   ,'        `.    \  /
   |  O        \___/  |
 ~^~^~^~^~^~^~^~^~^~^~^~^~
      """)
