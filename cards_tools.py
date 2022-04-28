def checkOne(stu):
    """
    This function was used to query one.If wasn't find a data you need, it will print "未查询到相关数据"
    :param stu: inputted data
    :return: null
    @author GXJ
    """
    # validate the entered list
    name = input("请输入学生姓名：")
    for s in stu:
        if s["name"] == name:
            print("姓名:%s  电话:%s  QQ:%s  邮箱:%s" % (s["name"], s["phone"], s["qq"], s["email"]), end="\n")
            while 1:
                print("*" * 50, end='\n')
                operation = int(input("请输入下一步操作1：修改名片  2：删除名片  3：返回上一级:"))
                print("*" * 50, end='\n')
                if operation == 1:
                    alterUserInfo(stu, stu.index(s), name)
                elif operation == 2:
                    deleteOne(stu, stu.index(s))
                elif operation == 3:
                    return
    print("未查询到相关数据")
    return


def checkAll(stuList):
    """
    This function was used to query all data in student list
    :param stuList: inputted student list
    :return: null
    @author GXJ
    """
    for stu in stuList:
        print("姓名:%s  电话:%s  QQ:%s  邮箱:%s" % (stu["name"], stu["phone"], stu["qq"], stu["email"]), end="\n")
    print("以上为所有数据")


def add_student(stu_list):
    """
    add student maps to list
    :return: a student map
    @author GXJ
    """
    print("请输入相关数据")
    name = input("姓名：")
    phone = input("电话：")
    qq = input("QQ：")
    email = input("邮件：")
    stu_list.append({
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    })
    print("%s 添加成功" % name)


def deleteOne(stu, index):
    """
    delete an item by name
    :return: null
    @author:GXJ
    """
    stu.remove(stu[index])
    print("删除完成")
    return


def alterUserInfo(stu_list, index, name):
    for i in stu_list:
        if i["name"] == name:
            i["name"] = input("姓名：")
            i["phone"] = input("电话：")
            i["qq"] = input("QQ：")
            i["email"] = input("邮件：")
            print("修改成功")
            break
