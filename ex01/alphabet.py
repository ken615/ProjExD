import random
from re import A

#グローバル変数
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#アルファベット
tgt = 10#対象文字数
lose = 2#欠損文字数
re = 5#最大繰り返し回数
now = 0#現在の繰り返し番号


#main関数
def main():
    global re, now
    while now < re:#最大繰り返し回数だけ繰り返す。
        q = question()
        if answer(q):
            break#正解ならwhile文を抜ける
        else:
            now += 1
            continue#不正解なら次の繰り返しに移行する
        

#question関数
def question():
    global alphabet, tgt, lose

    target = random.sample(alphabet, tgt)#10個のアルファベットのリスト
    lost_lit = random.sample(target, lose)#targetリストから選ばれた2個のアルファベットのリスト

    print("対象文字")
    for i in range(len(target)):
        print(target[i], end = " ")#targetリストの要素を一つずつ一行に表示
    print()#一行改行

    for i in range(lose):#欠損文字数分繰り返す
        target.remove(lost_lit[i])#targetから欠損文字を消去する
    random.shuffle(target)

    print("表示文字")
    for i in range(len(target)):
        print(target[i], end = " ")#欠損させたtargetリストの要素を一行に表示
    print()#一行改行

    return lost_lit#lost_litリストをかえす


#answer関数
def answer(question):
    global lose

    #欠損文字数の解答と評価
    try:
        num_ans = int(input("欠損文字はいくつあるでしょうか？"))
    except ValueError:
        print("整数を入力してください")
        return 0
    if num_ans == lose:#解答の評価
        print("せいかいです！それでは、具体的に欠損文字を一つずつ答えてください。")
    else:
        print("ふせいかいです！またチャレンジしてくださいね")
        return 0
    
    #欠損文字の解答と評価
    lit_ans1 = input("一つ目の文字を入力してください。")
    if lit_ans1 in question:#lit_ans1がquestionリスト内にあるなら
        pass
    else:
        print("ふせいかいです！またチャレンジしてくださいね")
        return 0
    question.remove(lit_ans1)#lit_ans1をquestionリスト内から消去する。
    
    lit_ans2 = input("二つ目の文字を入力してください。")
    if lit_ans2 in question:#lit_ans2がquestionリスト内にあるなら
        print("せいかいです！")
        return True
    else:
        print("ふせいかいです！またチャレンジしてくださいね")
        return 0

if __name__ == "__main__":
    main()























    """
    i = 0#問題の繰り返し番号
    while (i < max_repeat):
        print("対象文字 : ")
        target = make_target(alphabet, num_tgt)
        for i in range(len(target)):
            print(target[i], end = " ")#対象文字の表示
        print()
        print("表示文字 : ")
        display = lose_target(num_lost, alphabet, target)
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
            print("正解です。素晴らしい！!")
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
    tgt_lose_list = [target, lose_list]
        
    return tgt_lose_list

if __name__ == "__main__":
    main()
    """
