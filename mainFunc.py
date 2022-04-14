"""
student management system main function
@author GXJ
"""
import checkingFunction
import re

print("*" * 50)
print("欢迎使用【名片管理系统】")
print("1.新建名片")
print("2.显示全部")
print("3.查询名片")
print("4.删除名片")
print("0.退出系统")
print("*" * 50)
stu_list = []

while 1:
    operation = input("请选择操作：")
    if not re.match("^[0-4]{1}$", operation):
        print("没有此操作")
        continue
    operation = int(operation)
    if operation == 1:
        stu_list.append(checkingFunction.add_student())
        print("添加完成")
    elif operation == 2 and len(stu_list) > 0:
        checkingFunction.checkAll(stu_list)
    elif operation == 3 and len(stu_list) > 0:
        checkingFunction.checkOne(stu_list)
    elif operation == 4 and len(stu_list) > 0:
        checkingFunction.deleteOne(stu_list)
    elif operation == 0:
        print("感谢使用本系统")
        break
    else:
        print("列表为空")
