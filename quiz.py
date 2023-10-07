import time
score=0
Total_time=60
Time=input('Time left = 60 seconds....')
Start_time=time.time()
Question_1=input('Who was the first president of india?'
        '\n A.Ram nath kovind'
        '\n B.pranab mukherjee'
        '\n C.Dr.rajendra prasad'
        '\n D.A.P.J Abdul kalam')
Ending_time=time.time()
time_taken=Ending_time-Start_time
Total_time=Total_time-time_taken
if Total_time<=0:
        print('Time''s up!!!!!')
        exit()
ans=input('answer:-')

if ans=='C':
        print('correct answer')
        score=score+1
        print(score)
else:
        print('wrong answer')
Start_time=time.time()
Question_2=input('What is the capital of india?'
        '\n A.Delhi'
        '\n B.Kolkata'
        '\n C.Chennai'
        '\n D.Mumbai')
Ending_time=time.time()
time_taken=Ending_time-Start_time
Total_time=Total_time-time_taken
if Total_time<=0:
        print('Time''s up!!!!!')
        exit()
ans=input('answer:-')

if ans=='A':

        print('correct answer')
        score=score+1
        print(score)
else:
        print('Wrong answer')
Start_time=time.time()
Question_3=input('Who is current chief minister of kerala?'
        '\n A.K karunakaran'
        '\n B.Pinarayi vijayan'
        '\n C.A.k Atony'
        '\n D.Oomen Chandy')
Ending_time=time.time()
time_taken=Ending_time-Start_time
Total_time=Total_time-time_taken
if Total_time<=0:
        print('Time''s up!!!!!!')
        exit()
ans=input('answer:-')

if ans=='B':

        print('correct answer')
        score=score+1
        print(score)
else:
        print('wrong answer')
 

print('Quiz completed')
print('Total score =',score)

#time_duration = 15

#start_time = time.time()

#time_taken = time.time() - start_time
#if time_taken >= time_duration:
        #print("Time's up!")
        
