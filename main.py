import tools

while True:
    # 显示功能菜单
    tools.show_menu()
    # 得到用户输入
    action_str = input("请选择操作：")
    print("你选择的是【%s】" % action_str)
    # 如果输入为1，2，3，则为针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片的处理
        if action_str == "1":
            tools.new_card()
        # 显示全部名片的处理
        elif action_str == "2":
            tools.show_all()
        # 查询名片的处理
        else:
            tools.search_card()
    # 如果输入0，则退出
    elif action_str == "0":
        print("再见")
        break
    # 如果输入其他内容，提示输入错误
    else:
        print("输入错误，请重新输入")
