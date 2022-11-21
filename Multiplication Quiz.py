#This code created a program that poses 10 multiplication problems to the user, where the valid input is the problem’s correct answer.
import pyinputplus as pyip 
import random
import time
import sys
numberofquestions = 10 
correctAnwers = 0 
for questionNumber in range(numberofquestions):
    Q = questionNumber
    N1 = random.randint(0,9)
    N2 = random.randint(0,9)
    try:
        userinput = pyip.inputStr(
            prompt='{}{}{} {}{}{} {}\n'.format('Question Number',Q,':',N1,'x',N2,'='),
            timeout= 8, 
            limit= 3, 
            allowRegexes=['^%s$' %(N1*N2)],
            blockRegexes=[('.*', 'Incorrect!')]
        )
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    except KeyboardInterrupt:
        print('\nYou are welcome to play again')
        print('Your score is: %s / %s' % (correctAnwers, numberofquestions))
        sys.exit()
    else:   
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnwers += 1
    time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnwers, numberofquestions))
