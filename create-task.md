{% include base.html %}

<iframe frameborder="0" width="100%" height="450px" src="https://replit.com/@axiao05/hangman-create-task?lite=true"></iframe>

### Requirements:
* Take input from user, device, online data stream, or file
* Use at least one list/collection to manage data and program complexity
* At least one procedure with name, return type, and parameters
* Algorithm in procedure using selection, sequencing, and iteration
* Calls to procedure
* Instructions for output based on input and program functionality

### Idea: Hangman game. 
* User plays by entering letters and/or guessing the word (input)
* Word is randomly selected at start of program from list/dictionary that can be cleared/updated (custom word bank)
* Hangman procedure uses while loop with parameters win=false, also has counter for incorrect letter guesses
* Text output provides player with updates on wrong guesses, tries left, and what letters they have guessed

### Submission:
* ONE program file (Python or JS)
* One-minute runtime video with NO talking, only captions
* Short-answer questions, where you explain which parts of code meet requirements

***
### Allie's work
[Video demo](https://youtu.be/yKi6ucISImA)
[Alternate answer document](https://docs.google.com/document/d/1O2SFuxhPD1LO9QpGeQGzehhuvchrMXoD9n9z7bcuFhE/edit?usp=sharing)
1. The purpose of this program is to simulate a game of hangman, where a word is randomly selected from a predefined list of words and the user is given several tries to guess the word by guessing individual letters. The runtime video shows two games with different words, one winning game and one losing game. The inputs demonstrated are the user entering 1 to start playing and their letter guesses. The outputs demonstrated are the user’s updated guess strings, the hints, and the game result. 

2.  
```
word_list = ["slippery","marriage","system","overeat","requirement","ballot","democratic","producer","victory","therapist","layer","action","blue","parade","inch","dough","curve","potato","tomato","request","dream","apparatus","outer","carrot","hangman","stick","wheel","car","galaxy","chest","best","number","space","cry","shock","lightning","veteran","man","woman","presidential","goat", "horse", "soccer", "football", "person", "people", "someone", "boot", "shoes", "diet", "stop", "name", "mute", "unmute", "piano", "guitar", "cat", "dog", "bread", "chocolate", "cake", "loyalty", "punish", "throne", "fight", "student", "garfield", "movie", "million", "blubber", "minion", "lamb", "goofy", "funny","science", "weather", "fridge", "punish", "creed", "virus", "pandemic", "medic", "assault", "helper", "sniper", "explosion", "attract", "exclusive", "search", "available"]

word = random.choice(word_list)
```
The name of list is word_list. The words in the list represent the words that could be chosen for each round of the game. The program would be difficult to write without the list, because it would be almost impossible to manage the range of possible words without storing them in one list

3.  
```
def hangman():
  word = random.choice(word_list)
  c_l = []
  w_l = []
  win = False

  def add_to_hangman():
    misses = len(w_l)

  while win == False and len(w_l) != 7:
    display = ""

    guess = input("Guess a letter: ")
    if guess in word:
      c_l.append(guess)
    else:
      w_l.append(guess)
      add_to_hangman()

    display = ""

    if len(w_l) == 5 and len(c_l) < 4:
      print("Hint: " + random.choice(word))

    for letter in word:
        if letter in c_l:
            display += letter + " "
        else:
            display += "_" + " "
            win = False

    if len(c_l) == len(word):
      win = True

    print(display)

  if win == True:
      print("You WIN!")
  else:
    print("You LOSE :(")

if start == "1":
  hangman()
```
The hangman procedure contributes to the functionality of the code by ensuring that the developers and anyone else who may modify the code can see all of the functions in the proper sequence. 
The procedure constitutes the basic function of a hangman game by randomly choosing a word from the list and setting it as the unknown word, and creating two empty lists for right and wrong guesses. After each input the word is checked and if the letter appears in the string, it is added to the word display. When the number of wrong guesses exceeds 7 the player loses and the program terminates. Furthermore, there is also a hint system that gives the player a random letter in the word if they have 5 wrong guesses and less than 4 correct guesses.

4. The two calls in this case are different starting guesses when the word is “pandemic”. The first input is “a”. The program will check to see if it is a letter found in the word (which is it), so the program will add “a” to the empty list c_l as a correct guess, and display _a____. It will then prompt the user to enter another guess.
The second input is “q”, which is not in the word. The program will check and see that it isn’t, so it will add “q” to the empty list w_l as a wrong guess and display ______, then prompt the user to enter another guess.
