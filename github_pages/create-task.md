{% include base.html %}

<iframe frameborder="0" width="100%" height="450px" src="https://replit.com/@axiao05/hangman?lite=true"></iframe>

# Notice
This project is by Allie Xiao (me) for the Create Performance Task portion of the 2022 AP Computer Science Principles exam. The code portion is also documented on [Replit](https://replit.com/@axiao05/hangman#main.py).
This webpage, along with the [corresponding repository's wiki](https://github.com/xiaoa0/Data-Structures/wiki/Create-Task-documentation), documents my updated code, video, and written responses that I will use in my portfolio submission.
[This page](https://github.com/TheRadRabbidRabbit/Team-Lovelace/wiki/Tianbin-and-Allie-Create-Task-planning) serves as an archive for the early stages of development and was created **collaboratively** with Tianbin Liu.

While Tianbin may use some or all of the content contained in the last link in his submission, the work in the first two links and this file/page was created individually by me and will only be used by me. 

Anyone other than Tianbin attempting to submit material from the third link as their own work is committing plagiarism.
Anyone, _including_ Tianbin, attempting to submit material from the first two links as their own is committing plagiarism.

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
[Video demo](https://youtu.be/sYCiMiPG5uo)
[Alternate answer document](https://docs.google.com/document/d/1O2SFuxhPD1LO9QpGeQGzehhuvchrMXoD9n9z7bcuFhE/edit?usp=sharing)
1. The purpose of this program is to simulate a game of hangman, where a word is randomly selected from a predefined list of words and the user is given several tries to guess the word by entering individual letters. The runtime video shows two games with different words, one winning game and one losing game. The inputs demonstrated are the user’s guesses. The outputs demonstrated are the user’s updated guess strings and the game result. 

2.  
```
word_list = ["slippery","marriage","system","overeat","requirement","ballot","democratic","producer","victory","therapist","layer","action","blue","parade","inch","dough","curve","potato","tomato","request","dream","apparatus","outer","carrot","hangman","stick","wheel","car","galaxy","chest","best","number","space","cry","shock","lightning","veteran","man","woman","presidential","goat", "horse", "soccer", "football", "person", "people", "someone", "boot", "shoes", "diet", "stop", "name", "mute", "unmute", "piano", "guitar", "cat", "dog", "bread", "chocolate", "cake", "loyalty", "punish", "throne", "fight", "student", "garfield", "movie", "million", "blubber", "minion", "lamb", "goofy", "funny","science", "weather", "fridge", "punish", "creed", "virus", "pandemic", "medic", "assault", "helper", "sniper", "explosion", "attract", "exclusive", "search", "available"]
```
```
word = random.choice(word_list)
```
The name of the list used is word_list. The data in the list represents the possible words that the player must guess for the game. The program would be difficult to write without the list because it would be almost impossible to manage the range of possible words without storing them in a data structure.

3.  
```
def checker():
    nospaces = ''  # making word display a string
    word_string = nospaces.join(word_display)
  
    print(word_string)
    print("Wrong guesses: ", wrong_guesses)
    guess = input("Guess a letter: ").lower()

    if guess[0] in word: #using index to isolate first letter of input
        if guess[0] in word_display: #avoiding loop w/duplicate guesses
            wrong_guesses.append(guess)
            print("You have already guessed that letter. Guessing it again will add it to the list of wrong guesses.")
            if len(wrong_guesses) > 6:  # out of guesses (end)
                print("Oh no, you ran out of guesses :(")
                print("The answer was", word)
                return False
            else:
                return True
        else:
            for i in range (len(word)): #setting up to iterate through each character in word, checking for matching values
                if word[i] == guess:
                    word_display[i] = guess #replace entry at i in word display with guessed letter

        nospaces = ''  # making word display a string
        word_string = nospaces.join(word_display)
        if word == word_string:
            print(word_string)
            print("Congratulations, you win!")
            return False
        else:
            return True

    else: #adding to wrong_guesses
        wrong_guesses.append(guess)
        print("That letter is not in the word")
        if len(wrong_guesses) > 6:  # out of guesses (end)
            print("Oh no, you ran out of guesses :(")
            print("The answer was", word)
            return False
        else:
            return True
```
```
while status:
    status = checker()
```
The checker procedure contributes to the functionality of the code by managing potential inputs using branching if/else statements. It loops by returning the status boolean to continue the game until the player either guesses the word or runs out of guesses.
The procedure constitutes the basic function of a hangman game by randomly choosing a word from the list and setting it as the unknown word, then creating a list with underscores and a string with the same content. After each input the word is checked and if the guess appears in the string, it is added to the word display. The string is also checked to see if it matches the word (win condition). When the number of wrong guesses reaches 7 the player loses and the program terminates. Furthermore, the program also has a function to prevent an infinite loop, where entering a letter after it has already been confirmed to be correct will add that letter to the list of wrong guesses. 

4. The two calls in this case are different starting guesses when the word is “pandemic”. The first input is “a”. The condition being tested is whether “a” is found in the word “pandemic”. It is, so the program will replace the second entry in word_display to “a”, and display “_a______”. It will then prompt the user to enter another guess.
The second input is “q”. The condition being tested is whether “q” is found in the word “pandemic”. It is not, so the program will add “q” to the wrong_guesses list and display “________”. It will then prompt the user to enter another guess.
