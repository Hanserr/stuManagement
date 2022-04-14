import re


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
            return
        else:
            print("未查询到相关数据")
            return


def checkAll(stuList):
    """
    This function was used to query all data in student list
    :param stuList: inputted student list
    :return: null
    @author GXJ
    """
    if len(stuList) == 0:
        print("列表为空")
        return
    for stu in stuList:
        print("姓名:%s  电话:%s  QQ:%s  邮箱:%s" % (stu["name"], stu["phone"], stu["qq"], stu["email"]), end="\n")
    else:
        print("以上为所有数据")


def add_student():
    """
    add student maps to list
    :return: a student map
    @author GXJ
    """
    print("请输入相关数据")
    name = input("姓名：")
    phone = input("电话：")
    while not re.match("^1[3,4,5,7,8,9]\d{9}$", phone):
        print("手机号格式有误，请再次输入")
        phone = input("电话：")
    qq = input("QQ：")
    while not re.match("[1-9][0-9]{4,10}", qq):
        print("qq号格式有误，请再次输入")
        qq = input("qq：")
    email = input("邮件：")
    return {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }


def deleteOne(stu):
    """
    delete an item by name
    :return: null
    @author:GXJ
    """
    name = input("输入要删除学生的姓名:")
    for s in stu:
        if s["name"] == name:
            stu.remove(s)
            print("删除完成")
            return
    print("数据库未录入此人信息")
    return
