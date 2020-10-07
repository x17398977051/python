#写入文件
#open*(file_name,'w') 代表写入的意思 'r'读取模式 'w'写入模式 'a' 附加模式 'r+'读取写入模式

file_name = '2020-10-07.txt'

with open(file_name,'w') as file_object:
    file_object.write('人生苦短,我用Python\n')



#附加到文件
with open(file_name,'a') as file_object:
    file_object.write("人生苦短,我用JavaScript\n")
    file_object.write("人生苦短,我用Node.js\n")
