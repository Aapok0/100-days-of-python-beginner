# Hangman

A classic game of hangman, where you are given mystery word. One by one you guess letters in it. Right guess shows where those letters are and wrong one letters building the hangman piece by piece. You need to guess all the letters before the hangman is done.

## Flow of game

```mermaid
flowchart TB
    start[Welcome to hangman] --> word[Generate word for the game]
    word --> blanks[Generate blanks for the letters of the word]
    blanks --> letter[Player chooses letter]
    letter --> checkword{In the word?}

    checkword --> |Yes| position[Show letter positions]
    checkword --> |No| hangman[Piece to hangman]

    position --> checkfill{Are all the letters filled?}
    checkfill --> |Yes| win[Player wins]
    checkfill --> |No| letter

    hangman --> hanged{Is hangman built?}
    hanged --> |Yes| lose[Player loses]
    hanged --> |No| letter
```

## How to play

Clone the repository and run the hangman.py with a Python interpreter.

## [Course solution](https://replit.com/@appbrewery/Day-7-Hangman-Final)
