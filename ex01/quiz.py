import random
import datetime

def main():
    question_answer = [("サザエの旦那の名前は？", ["マスオ", "ますお"]),
                       ("カツオの妹の名前は？", ["ワカメ", "わかめ"]), 
                       ("タラオはカツオから見てどんな関係？", ["甥", "おい", "甥っ子", "おいっこ"])]
    num = random.randint(0,(len(question_answer) - 1))
    start = datetime.datetime.now()
    syutudai(question_answer, num)
    kaito(question_answer, num, start)

def syutudai(question_answer, num):
    question = question_answer[num][0]
    print(question)

def kaito(question_answer, num, start):
    kaito = input("解答する: ")
    if kaito in question_answer[num][1]:
        print("正解！")
    else:
        print("不正解!")
    finish = datetime.datetime.now()
    print(finish - start)

if __name__ == "__main__":
    main()
