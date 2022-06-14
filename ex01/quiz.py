
"""   
ans1 = input("問題:\nサザエの旦那の名前は？\n答えるんだ:")
if ans1 == "マスオ":
    print("正解！！！")
elif ans1 == "ますお":
    print("正解！！！")
else:
    print("出直してこい")

ans2 = input("問題:\nカツオの妹の名前は？\n答えるんだ:")
if ans2 == "ワカメ":
    print("正解！！！")
elif ans2 == "わかめ":
    print("正解！！！")
else:
    print("出直してこい")

ans3 = input("問題:\nタラオはカツオから見てどんな関係？\n答えるんだ:")
if ans3 == "甥":
    print("正解！！！")
elif ans3 == "おい":
    print("正解！！！")
elif ans3 == "甥っ子":
    print("正解！！！")
else:
    print("出直してこい")
 """       


a = "正解！！！"
b = "出直してこい"
quiz_list = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
for ans1 in quiz_list:
    ans = input(f"問題:\n{ans1}\n答えるんだ:")
    if ans == "マスオ" and "ますお":
        print(a)
    elif ans == "わかめ" and "ワカメ":
        print(a)
    elif ans == "甥" and "おい" and "甥っ子":
        print(a)
    else:
        print(b)

