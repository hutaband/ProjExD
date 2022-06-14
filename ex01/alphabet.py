import random
num = 10 #文字数
a1 = ""
a2 = ""
lost = random.randint(0,10)
lost2 = random.randint(0,10)
m = [chr(i) for i in range(65,91)] #for文でリストの作成
ran_alph = random.sample(m,k=num) #重複なしでnum個ランダムで取り出し
a = " ".join(ran_alph) #型変形
print(f"対象文字:\n{a}")
b = ran_alph.pop(lost) #リストから文字を取り除く
b = ran_alph.pop(lost2)
b = " ".join(ran_alph)
print(f"表示文字:\n{b}")
ans = input("欠損文字はいくつあるでしょうか？:") #参照
if ans == "2":
    print("正解です、それでは、具体的に欠損文字を１つずつ入力してください")
ans2 = input("1つ目の文字を入力してください:") #値を入力
ans3 = input("2つ目の文字を入力してください:")
if ans2 == a1 and ans3 == a2: #演算
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



