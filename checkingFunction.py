def checkO(stu):
    """
    This function was used to query one.If wasn't find a data you need, it will print "未查询到相关数据"
    :param stu: inputted data
    :return: null
    @author GXJ
    """
    # validate the entered list
    if len(stu) == 0:
        print("暂无数据,请先添加数据")
        return
    name = input("请输入学生姓名：")
    for s in stu:
        if s["name"] == name:
            print("姓名:%s  电话:%s  QQ:%s  邮箱:%s" % (s["name"], s["phone"], s["qq"], s["email"]), end="\t")
            return
        else:
            print("未查询到相关数据")
            return


def checkAll(stuList):
    """
    This function was used to query all datas in student list
    :param stuList: inputted student list
    :return: null
    @author GXJ
    """
    if len(stuList) == 0:
        print("列表为空")
        return
    for stu in stuList:
        print("姓名:%s  电话:%s  QQ:%s  邮箱:%s" % (stu["name"], stu["phone"], stu["qq"], stu["email"]))
    else:
        print("以上为所有数据")


def add_student():
    """
    add student maps to list
    :return: a student map
    @author GXJ
    """
    print("请输入相关数据：")
    name = input("姓名：")
    phone = input("电话：")
    qq = input("QQ：")
    email = input("邮件：")
    return {"name": name,
            "phone": phone,
            "qq": qq,
            "email": email}
