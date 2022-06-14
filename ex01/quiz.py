import random

def main():
    question_answer = [("サザエの旦那の名前は？", ["マスオ", "ますお"]),
                       ("カツオの妹の名前は？", ["ワカメ", "わかめ"]), 
                       ("タラオはカツオから見てどんな関係？", ["甥", "おい", "甥っ子", "おいっこ"])]
    num = random.randint(0,(len(question_answer) - 1))
    syutudai(question_answer, num)
    kaito(question_answer, num)

def syutudai(question_answer, num):
    question = question_answer[num][0]
    print(question)

def kaito(question_answer, num):
    kaito = input("解答する: ")
    if kaito in question_answer[num][1]:
        print("正解！")
    else:
        print("不正解!")

if __name__ == "__main__":
    main()
