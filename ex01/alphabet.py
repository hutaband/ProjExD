import random
num = 10
a1 = ""
a2 = ""
lost = random.randint(0,10)
lost2 = random.randint(0,10)
m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alph_list = list(m)
ran_alph = random.sample(alph_list,k=num)
a = " ".join(ran_alph)
print(f"対象文字:\n{a}")
b = ran_alph.pop(lost) 
b = ran_alph.pop(lost2)
b = " ".join(ran_alph)
print(f"表示文字:\n{b}")
ans = input("欠損文字はいくつあるでしょうか？:")
if ans == "2":
    print("正解です、それでは、具体的に欠損文字を１つずつ入力してください")
ans2 = input("1つ目の文字を入力してください:")
ans3 = input("2つ目の文字を入力してください:")
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



