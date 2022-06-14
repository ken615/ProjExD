import random

#グローバル変数
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#アルファベット
num_tgt = 10#対象文字数
num_lost = 2#欠損文字数
max_repeat = 5#最大繰り返し回数

def main():
    i = 0#問題の繰り返し番号
    while (i < max_repeat):
        print("対象文字 : ")
        display = make_target(alphabet, num_tgt)
        for i in range(len(display)):
            print(display[i], end = " ")#対象文字の表示
        print("表示文字 : ")
        for i in range(len(display)):
            print(display[i], end = " ")
        print()
        ans = input("欠損文字はいくつあるでしょうか？ : ")
        if ans == num_lost:
            print("正解です。それでは、具体的に欠損文字を一つずつ入力してください。")
        else:
            continue
        lose1 = input("一つ目の文字を入力してください。 : ")
        lose2 = input("二つ目の文字を入力してください。 : ")
        seikai = lose_target(num_lost, alphabet, display)
        if (lose1 in seikai & lose2 in seikai):
            print("正解です。素晴らしい！")
            break
        else:
            print("不正解です。またチャレンジしてください。")#不正解と表示する
        i += 1

def make_target(target, num):#アルファベットと対象文字数を引数に取る
    display = []#対象文字
    for i in range(num):
        display.append(target[random.randint(0, (len(target) - 1))])#対象文字をnum_tgtの数だけ入れる
    return display#対象文字をかえす

def lose_target(num, alphabet, target):#欠損文字数とアルファベットと対象文字を引数に取る
    lose_list = []
    for i in range(num):
        lose_idx = alphabet[random.randint(0, (len(alphabet) - 1))]
        for j in range(target):
            if target[j] == alphabet[lose_idx]:
                lose_list.append(target.pop(j))
    return lose_list

if __name__ == "__main__":
    main()
