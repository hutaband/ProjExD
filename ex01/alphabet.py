import random
num = 10 #文字数
a1 = ""
a2 = ""
lost = random.randint(0,10) #1~10のランダム数
lost2 = random.randint(0,10)
m = [chr(i) for i in range(65,91)] #A~Zのリスト
ran_alph = random.sample(m,k=num) #ランダムで10個のアルファベットリスト
a = " ".join(ran_alph)#型を変える
print(f"対象文字:\n{a}")
b = ran_alph.pop(lost) #欠損文字1文字目
b = ran_alph.pop(lost2) #欠損文字2文字目
b = " ".join(ran_alph)
print(f"表示文字:\n{b}")
ans = input("欠損文字はいくつあるでしょうか？:")#文字数の判定
if ans == "2":
    print("正解です、それでは、具体的に欠損文字を１つずつ入力してください")
ans2 = input("1つ目の文字を入力してください:")#文字の判定
ans3 = input("2つ目の文字を入力してください:")#文字の判定
if ans2 == a1 and ans3 == a2:
    print("おめでとう")
else:
    print("不正解です、またチャレンジしてください")
    
    
    #while True:
    #    ans2 = input("正解です、それでは、具体的に欠損文字を１つずつ入力してください\n１つ目の文字を入力してください:")
    #    if ans2 == "A":
    #        continue
    #    ans3 = input("２つ目の文字を入力してください:")
    #    if ans3 == "B":
    #        print("おめでとう")
    #    break



