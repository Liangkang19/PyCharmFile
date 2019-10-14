import easygui   # 先引入easygui模块
while 1:
    easygui.msgbox('大家好！欢迎来到赶海天堂！')
    message = '请选择人物'
    title = '赶海天堂'
    choices = ['老四', '阿峰', '阿雄']
    choice = easygui.choicebox(message, title, choices)
    easygui.msgbox('你的选择是:' + str(choice))
    if str(choice) == '老四':
        easygui.msgbox('大家好！我是老四！')
        break
    if str(choice) == '阿峰':
        easygui.msgbox('今天是要发财的节奏！')
        break
    if str(choice) == '阿雄':
        easygui.msgbox('这么小的一条石九公啊！')
        break



