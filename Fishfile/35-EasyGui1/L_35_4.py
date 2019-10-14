# 提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容
import easygui
import os
file_path = easygui.fileopenbox()               # 打开当前文件夹下的文件选择框(返回文件路径)
with open(file_path) as old_file:                     # 将该文本文件用old_text来表示
    title1 = os.path.basename(file_path)        # 去掉文件路径，返回文件名
    message1 = ('文件[%s]的内容如下:' % title1)
    old_text = old_file.read()                           # 读入文件
    new_text = easygui.textbox(message1, title1, old_text)
if old_text != new_text[:-1]:
    choice1 = easygui.buttonbox('检测到文件内容已发生改变，请选择以下操作', '警告！', ('重新保存', '不保存', '另存为'))
    if choice1 == '重新保存':
        with open(file_path, 'w') as old_file:
            old_file.write(new_text[:-1])
    if choice1 == '不保存':
        pass
    if choice1 == '另存为':
        another_path = easygui.filesavebox(default='.txt')
        if os.path.splitext(another_path)[1] != '.txt':
            another_path = another_path + '.txt'
        with open(another_path, 'w') as new_file:
            new_file.write(new_text[:-1])



