import os
'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：531509025
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
# Open file
f = open("new_2007_train.txt",'w')
fileHandler  =  open  ("2007_train.txt",  "r")
while  True:
    # Get next line from file
    line  =  fileHandler.readline()
    # If line is empty then end of file reached
    if  not  line  :
        break;
    print(type(line))
    line = line[46:]
    line = "DL/"+line
    f.write(line)
    print(line.strip())
    # Close Close
fileHandler.close()
f.close()
