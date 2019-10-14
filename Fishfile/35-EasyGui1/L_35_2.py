import easygui
print('-------------我爱鱼c工作室--------------')
temp = easygui.enterbox("猜一下小甲鱼想的是哪个数字:", '数字小游戏')
guess = int(temp)
if guess == 8:
    easygui.msgbox('卧槽，你是小甲鱼的心里蛔虫吗？', '数字小游戏')
    easygui.msgbox('哼，猜中了也没有奖励！', '数字小游戏')
else:
    easygui.msgbox('猜错啦，小甲鱼现在心里想的是8！', '数字小游戏')

easygui.msgbox('游戏结束！', '数字小游戏')
