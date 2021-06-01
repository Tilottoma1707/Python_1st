Intro=input("Enter Your Introduction")
print(Intro)
wordcount=0
characterCount=0

for i in Intro :
    characterCount=characterCount+1
    if i== ' ':
        wordcount=wordcount+1
print(characterCount,wordcount)        