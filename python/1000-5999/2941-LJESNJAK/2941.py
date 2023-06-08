word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in word_list:
    word = word.replace(i, 'a')
    print(word)
print(len(word))