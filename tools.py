# 记录所有的名片的列表
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print()
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print()
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    qq_str = input("请输入qq号码：")
    email_str = input("请输入邮箱地址：")

    # 使用用户输入的信息建立一个名片
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 将名片添加到名片列表中
    card_list.append(card_dict)

    # 提示用户添加成功
    print("添加%s的名片成功！" % card_dict)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，若无就提示用户
    if len(card_list) == 0:
        print("当前无任何记录，请先添加名片！")
        return

    # 打印表头
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历名片依次输出信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片"""
    print("搜索名片")
    print("-" * 50)

    # 提示用户输入要搜索的姓名
    find_name = input("请输入要查找的姓名：")

    # 遍历名片列表，查询姓名，如果没有找到需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("success!")
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 针对找到的名片进行修改和删除操作
            deal_card(card_dict)
            break
    else:
        print("sorry,查找%s失败" % find_name)


def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict: 查找到的名片
    """
    print(find_dict)
    action_str = input("请选择操作"
                       "【1】 修改 【2】 删除 【0】 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：（回车不修改）")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：（回车不修改）")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq：（回车不修改）")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：（回车不修改）")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入内容，就返回内容，否则返回原有的值
    """
    # 提示用户输入内容，针对用户的输入判断
    result_str = input(tip_message)
    # 如果输入内容直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果没有输入内容，返回字典原有内容
    else:
        return dict_value
