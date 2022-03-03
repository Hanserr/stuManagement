def add_student():
    print("请输入相关数据：")
    name = input("姓名：")
    phone = input("电话：")
    qq = input("QQ：")
    email = input("邮件：")
    return {"name": name,
            "phone": phone,
            "qq": qq,
            "email": email}
