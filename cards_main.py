"""
student management system main function
@author GXJ
"""
import cards_tools
import re

stu_list = []
while 1:
    cards_tools.showMenu()
    operation = input("请选择操作：")
    if operation not in ["1", "2", "3", "0"]:
        print("没有此操作")
        continue
    if operation == "1":
        cards_tools.addStudent(stu_list)
    elif operation == "2" and len(stu_list) > 0:
        cards_tools.checkAll(stu_list)
    elif operation == "3" and len(stu_list) > 0:
        cards_tools.checkOne(stu_list)
    elif operation == "0":
        print("感谢使用本系统")
        break
    else:
        print("列表为空,请先添加用户")
