def checkAll(stuList):
    """
    This function was used to query all datas in student list
    :param stuList:
    :return:
    """
    if len(stuList) == 0:
        print("列表为空")
        return
    for stu in stuList:
        print("姓名:%s  电话:%s  QQ:%s  邮箱:%s" % (stu["name"], stu["phone"], stu["qq"], stu["email"]))
    else:
        print("以上为所有数据")