def checkO(stu):
    """
    This function was used to query one.If wasn't find a data you need, it will print "未查询到相关数据"
    :param stu: inputted data
    :return: null
    """
    name = input("请输入学生姓名：")
    for s in stu:
        if s["name"] == name:
            print("姓名:%s  电话:%s  QQ:%s  邮箱:%s" % (s["name"], s["phone"], s["qq"], s["email"]))
            break
        else:
            print("未查询到相关数据")
