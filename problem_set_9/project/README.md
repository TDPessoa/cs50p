# Math Game
---
### Video demo: [CS50p - TDPessoa's final project](https://youtu.be/YU4K8el5EJc)
### Author: TDPessoa
### My GitHub: [@TDPessoa](https://github.com/TDPessoa)
---
#### Description:
This is a script that will generate a terminal text-based math's game.<br>
The script will contain 2 main functionalities, accessed via command-line arguments.<br>
When chosen to play the game and the level wanted, it will prompt a problem for the user to say it's answer, for each correct answer the user scores.<br>
At the end of the run, the script will ask for 3 letters for identification and record the user's score.<br>
The levels, as best described at 'usage', are easy, medium, hard and endless.<br>
When chosen score, the script will printout the top 10 highest scores for the required level.<br>
When chosen help, the script will printout it's usage.

##### check50 results:
:) README.md exists  
:) final project details  
:) project.py exists  
:) main function exists  
:) implemented at least 3 top-level functions other than main  
:) each function other than main accompanied with a unit test  
#####Functionalities:
1. Expect command-line arguments, using `sys.argv`:
    ```
    usage: python project.py [ options ]
        options:
            -p, --play [ level ]
                level:                      
                        1 or "easy"         10 Problems of addition and subtraction
                        2 or "medium"       20 Problems of addition, subtraction and multiplication
                        3 or "hard"         30 Problems of addition, subtraction, multiplication and division
                        4 or "endless"      Endless quantity of Medium difficulty but, if three incorrect answers where given, the run ends
            -s, --score [ level ]
                level:
                    1, 2, 3, 4              Will print in Terminal the Top 10 highest scores for that level
            -h, --help
    ```
2. When `-p, --play [ level ]`:
    <br>
    The script will generate 2 values using `random.randint`, and, with `random.choice` select from the list of operators.
    <br>
    Then, print in the Terminal the problem.(ie. "34 + 55 = ")
    <br>
    The range of values will go from 0(zero) to: 
    + Easy: 9
    + Medium: 99
    + Hard: 999
    + Endless: 99
    <br>
    When the session finishes, the score will be stored at `score_{level}.txt` file.
3. When `-s, --score [ level ]`:
    <br>
    The script will read the required level's scores at `score_{level}.txt` file.
4. When `-h, --help`:
    <br>
    The script will output the usage message from before.
    <br><br>
#####Imported Libraries:
1. random:
    <br>
    choice: For selecting the problem's mathematical operator from a list. 
    <br>
    randint: For generate the 2 values for the problem.
    <br>
    seed: For tests, as it's needed to fixate the values generated.
    <br>
2. sys.argv: For extracting the command-line argument.
3. pytest.raises: For `Exception`s tests in `project_test.py`.
    <br><br>
#####Functions:
1. initializer(command): 
    ```
    Will handle the command_line argument and return the required way.
    
    :param command: str, to be extracted the values
    :return:  a str and/or an int =>    -p, --play  -> 'p', 'level'
                                        -s, --score -> 's', 'level'
                                        -h, --help  -> 'h'   
    ```    
2. generate(level, test=False):
    ```
    Will generate the values of two variables and choose the operator
    
    Will always list the greater value as num1.
    When:
        In medium difficulty:
            Will set the multiplier as it's decimal case.
        In hard difficult:
            Will set the divisor as it's decimal case
                And re-draw if the answer isn't an integer.
            Will set the multiplier as its tenths and decimal cases.
    
    :param level:   int, to be used as template for drawing the values.
    :param test:   Bool, only used in test_project
    :return:        int | int | str -> as: num1, num2, operator
    ```
3. question(x, op, y, answer):
    ```
    Will receive the values and operator of the problem with the answer to be verified. 
    
    :param x:       int, first value of the problem
    :param y:       int, second value of the peoblem
    :param op:      str, from ('+', '-', '*', '/')
    :param answer:  int, user's inputted answer
    :return:        Bool -> if f'x {op} y' == answer 
   ```
4. score(level, action, _score=None):
    ```
    Will open the score file to the specified level and record the scored points or print out the current stored rank.
    If the score_file has anything out of the ordinary(ie. less then 10 lines or was not found) it will be re-writen

   :param level: int -> 1, 2, 3, 4
   :param action: str -> 's' -> reads score | 'p' -> records score | 'r' -> restores score
   :param _score: None | int
   :return: None 
   ```
