# -*- coding: cp936 -*-

# 创建一个函数，统计一个文档有多少个单词

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','sidd.txt', 'alice.txt']
for filename in filenames:
    count_words(filename)

# 代码运行出现错误时，什么都不发生，继续运行剩余的代码，使用pass
print("\n")
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','sidd.txt', 'alice.txt']
for filename in filenames:
    count_words(filename)
