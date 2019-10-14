import easygui
easygui.egdemo()  # 可调出eg里的各种函数的功能框
easygui.msgbox('Hello，world(内容)', '赶海人生(标题)')
easygui.msgbox(msg='内容参数', title='标题参数', ok_button='按键参数')     # 确定按钮框
easygui.ccbox(msg='内容参数?', title='标题参数', choices=('Yes', 'No'))    # 选择判断框
easygui.buttonbox(msg='请选择人物?', title='赶海人生', choices=('老四', '阿峰', '阿雄'))  # 多按钮设置框
easygui.boolbox(msg='请选择人物?', title='赶海人生', choices=('Yes', 'No'))  # 选择判断框
easygui.buttonbox(msg='请选择人物?', title='赶海人生', image='Pic_35.png', choices=('老四', '阿峰', '阿雄'))
easygui.choicebox()        # 选择框
easygui.multchoicebox()    # 多选框
easygui.enterbox()         # 输入框
easygui.integerbox()       # 范围输入框
easygui.multenterbox()     # 多输入框
easygui.passwordbox()      # 密码输入框
easygui.multpasswordbox()  # 多维密码输入框
easygui.textbox()          # 文本显示框
easygui.codebox()          # 等宽字体显示框
easygui.diropenbox()       # 目录输出框
easygui.fileopenbox()      # 打开文件框(返回文件路径)
easygui.filesavebox()      # 文件保存框(选择文件保存路径)
easygui.exceptionbox()     # 异常处理框
