#while loop
run = True
while run:
    user_input = int(input('Enter Number: '))
    if user_input == 7:
        print('You won!')
        run = False
    else:
        print('try again!')
        continue1
        
    
"""for loop
attempt = 5
for i in range(5):
    user_input = int(input('Enter Number: '))

    if user_input == 7:
        print('You won!')
        break
    else:
        print(f'Try again! {attempt} left.')
        attempt -= 1
        continue
"""

"""random number
import random

num = random.randint(0, 10)
print('Number:',num)
attempt = 4 
msg = 'You Lost!'   

while attempt > 0:
    user_input = int(input('Enter Number: '))

    if user_input == num:
        msg = 'You Won!'
        break
    else:
        print(f'Try again! {attempt} attempt left.')
        attempt -= 1
        continue

print(msg)
"""


    
   


    
