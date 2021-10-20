import os
import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
lives = 6
previously_guessed = ""

for step in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    
    if guess in previously_guessed:
      print(f"You've already chosen {guess}, please try a different letter: ")
    else:
      previously_guessed += guess

      for position in range(word_length):
          if chosen_word[position] == guess:
              display[position]=chosen_word[position]
      print(f"{' '.join(display)}")
         
      if guess not in chosen_word:
        print(hangman_art.stages[lives]) 
        print(f"You guessed {guess}, which is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(hangman_art.stages[lives])
            print(f"You Lose!, the word was actually {chosen_word}!") 

      if not "_" in display:
        end_of_game = True
        print(f"You Win!, the word was indeed {chosen_word}!")
