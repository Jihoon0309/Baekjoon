martix=[]

for _ in range(5):
    word=input()
    word_list=list(word)
    martix.append(word_list)


for i in range(15):
    for j in range(len(martix)):
        try:
            print(martix[j][i], end='')
        except:
            pass
print()