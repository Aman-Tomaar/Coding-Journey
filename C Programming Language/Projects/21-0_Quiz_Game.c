#include <stdio.h>
#include <ctype.h>  // Required for toupper()
#include <string.h> // Best practice for string arrays

int main() {
    char questions[][100] = {
        "1. What is the largest planet in the solar system?",
        "2. What is the hottest planet?",
        "3. What planet has the most moons?",
        "4. Is the Earth flat?"
    };

    char options[][100] = {
        "A. Jupiter \nB. Saturn \nC. Uranus \nD. Neptune",
        "A. Mercury \nB. Venus \nC. Earth \nD. Mars",
        "A. Earth \nB. Mars \nC. Jupiter \nD. Saturn",
        "A. Yes \nB. No \nC. Maybe \nD. Sometimes"
    };

    char answerKey[] = {'A', 'B', 'D', 'B'};
    int numberOfQuestions = sizeof(questions) / sizeof(questions[0]);
    char guess;
    int score = 0;

    printf("**** QUIZ GAME ****\n\n");

    for(int i = 0; i < numberOfQuestions; i++) {
        printf("%s\n", questions[i]);
        printf("%s\n", options[i]);
        
        printf("Enter your choice: ");
        scanf(" %c", &guess); // The leading space handles newline characters cleanly
        
        guess = toupper(guess); // Converts lowercase input to uppercase
        
        if(guess == answerKey[i]) {
            printf("CORRECT!\n\n");
            score++;
        } else {
            printf("WRONG! The correct answer was %c.\n\n", answerKey[i]);
        }
    }

    printf("X--------------------------------X\n");
    printf("Your final score is: %d/%d\n", score, numberOfQuestions);
    printf("X--------------------------------X\n");

    return 0;
}