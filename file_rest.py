from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.reset()
test_list = open('test-fragment.txt',encoding='utf-8')

print(type(test_list))