# hangman_game

이 게임은 우리가 잘아는 행맨 게임입니다.

게임 방식:
   방식은  단어의 알파벳 갯수에 따른 '-'가 주어집니다.

   플레이어는 알파벳 1개씩 입력후 이것이 맞는지 틀린지 출력합니다.

   10번의 기회가 있고 10번째 틀리면 game over 됩니다.

-----------------------------------------------------------------------------------------

여러분이 원하는 단어를 words 리스트에 넣으시면 랜덤으로 1개를 뽑아 게임의 단어로 선정합니다.

     words = ["apple","banana","orange","collagen","economics","global"]

test_hangman 함수를 사용하여 단어의 알파벳과 플레이어의 알파벳 입력이 맞는지 검증합니다.
     
     def test_hangman():

주석으로 주요 기능을 써두었으니 참고하세요!
