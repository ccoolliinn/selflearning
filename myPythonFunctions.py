from random import randint
from os import remove, rename

def generateQuestion():

    operandList = [0, 0, 0, 0, 0]
    operatorList = ['', '', '', '']
    operatorDict = {1:' + ', 2:' - ', 3:'*', 4:'/',5:'**'}
    result=60
    while result<=0 or result >=20:
        for index in range(0, 5):
            operandList[index] = randint(1, 9)

        for index in range(0, 4):
            if index > 0 and operatorList[index-1] != '**':
                operator = operatorDict[randint(1, 5)]
            else:
                operator = operatorDict[randint(1, 4)]

            operatorList[index] = operator
        #接下来考虑“（）”的加入：
        openbracket=randint(0,3)
        closebracket=randint(openbracket+1,4)
        if openbracket==0:
            questionString='('+str(operandList[0])
        else:
            questionString=str(operandList[0])
        for index in range(1,5):
            if index ==openbracket:
                questionString=questionString+operatorList[index-1]+'('+str(operandList[index])
            elif index==closebracket:
                   questionString=questionString+operatorList[index-1]+str(operandList[index])+')'
            else:
                   questionString = questionString + operatorList[index - 1] + str(operandList[index])

        result = round(eval(questionString),2)
        #以上的循环值得学习，利用循环卡条件
    questionString = questionString.replace("**", "^")
    print('\n' + questionString)
    userResult = input('Answer: ')

    while True:
        try:
            if float(userResult) == result:
                print ("So Smart")
                return 1
            else:
                print ("Sorry, wrong answer. The correct answer is", result)
                return 0
        except Exception as e:
            print ("You did not enter a number. Please try again.")
            userResult = input('Answer: ')
                        

def getUserScore(userName):

    try:
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(',')
            if content[0] == userName:
                input.close()
                return content[1]

        input.close()
        return "-1"
    except IOError:
        print ("\nFile userScores.txt not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return "-1"


def updateUserPoints(newUser, userName, score):
    
    if newUser:

        input = open('userScores.txt', 'a')
        input.write('\n' + userName + ', ' + score)
        input.close()
    else:

        input = open('userScores.txt', 'r')
        output = open('userScores.tmp', 'w')

        for line in input:
            content = line.split(',')
            if content[0] == userName:
                content[1] = score
                line = content[0] + ', ' + content[1] + '\n'            

            output.write(line)

        input.close()
        output.close()
    
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
