import random

def askforanswer( nrcorrect, nr1, nr2 ):
    while True:
        inputstring = input( "question {}: please calculate {} times {} ". format( nrcorrect, nr1, nr2 ) )
        try:
            answer = int( inputstring )
            return answer
        except ValueError:
            print("Please, try again! You entered invalid input:\n")

def exam():
    nrcorrect = 1;
    upperbound = 20;
    while nrcorrect<6:
        nr1 = random.randrange( upperbound )
        nr2 = random.randrange( upperbound )
        correct = nr1 * nr2
        answer = askforanswer( nrcorrect, nr1, nr2 )
        if answer == correct:
            nrcorrect = nrcorrect+1
            print( "You are right!" )
        else:
            print( "Wrong!" )
            print( "The right answer is {}:". format( correct ) )
            nrcorrect = 1

    print( "Exam is over." )

