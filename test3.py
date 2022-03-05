"""
student management system main function
@author GXJ
"""
import checkingFunction

print("*" * 50)
print("欢迎使用【名片管理系统】")
print("1.新建名片")
print("2.显示全部")
print("3.查询名片")
print("0.退出系统")
print("*" * 50)
stu_list = []
flag = True

while flag:
    operation = int(input("请选择操作："))
    if operation == 1:
        stu_list.append(checkingFunction.add_student())
        print("添加完成")
    elif operation == 2:
        checkingFunction.checkAll(stu_list)
    elif operation == 3:
        checkingFunction.checkO(stu_list)
    elif operation == 0:
        print("感谢使用本系统")
        flag = False
    else:
        print("输入的操作有误！")
