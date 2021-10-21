
from random import *

# 리스트 원소의 합
def sumOfList(llist):
  sum = 0
  for n in llist:
    sum = sum + n
  return sum

# list
words = ["apple","banana","orange","collagen","economics","global","duck"]
alphabets = []
sums = [0,0]
texts = [0]
history_text =[]

def test_hangman():

   # 리스트에 있는 것중 1개를 선택
    i = 0
    word = choice(words)
    letters = " "

    # 답이 나올때 까지 반복
    while True:
        global succeed
        succeed = True
        

        for w in word:
            if w in letters:
                print(w,end=" ")          
                        
            else:
                print("_",end=" ")
                succeed = False

            
        if succeed :
            break

        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        letter = input("Input > ")
        texts.append(letter)
        history_text.append(letter)
        del texts[0]

        if letter not in letters:
            letters += letter

        for j in range(26):
            a = texts[0].count(alphabet[j]) # 입력받은값의 알파벳의 갯수를 세서 a에 저장한다. ex) ab= > 1 1 
            alphabets.append(a)  # alphabets 라는 빈 리스트에 a값을 추가한다.  
        sum = sumOfList(alphabets) # a의 합을 구해서 sum 변수에 저장한다.
        sums.append(sum) # 이를 sums 리스트에 추가한다.
        del sums[0] # sums의 첫번째 값을 없애준다.

        sums_dif = sums[1] - sums[0]  # 입력값의 알파벳 갯수는 sums[1]에 저장되고 만약 이 차이가 2와 같거나 클 경우 즉 한개의 알파벳이 아닐경우

        if sums_dif >= 2: 
            print("1개의 알파벳만 입력할수 있습니다.")
            letters = " "
            continue
        
        if texts[0] == '' :
            print("1개 이상의 알파벳을 입력해주세요.")
            continue

        print()
    
        
        # word 안에 text가 있다면 correct, 없다면 wrong
        if letter in word and letter is not None:
            print("Correct!")

        else:
            i += 1
            print("Wrong!: " +str(i))
                    
                
            if i == 10:
                print("Game Over")
                break


test_hangman()
            
                
           
        

        
                         
    
   
    
    
