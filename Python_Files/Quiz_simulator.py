from Projects import Quiz
import pygame
quiz = Quiz()
quiz.begining()
while True:
    key = input("> ").lower()
    if key == "Done":
        break
    print(quiz[key])