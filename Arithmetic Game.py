import random
import time


class ArithmeticGame:
    def __init__(self, num_questions):
        self.num_questions = num_questions

    def generate_questions(self):
        operand1 = random.randint(0, 30)
        operand2 = random.randint(0, 30)
        operand = random.choice(['+', '-', '*', '//'])
        if operand == '+':
            answer = operand1 + operand2
        if operand == '-':
            answer = operand1 - operand2
        if operand == '*':
            answer = operand1 * operand2
        if operand == '//':
            answer = operand1 // operand2
        question = str(operand1) + ' ' + str(operand) + ' ' + str(operand2)
        return question, answer

    def play_game(self):
        start_time = time.time()
        correct_ans = 0
        for i in range(self.num_questions):
            question, answer = self.generate_questions()
            print(question)
            user_answer = int(input('What is your answer?: '))
            if answer == user_answer:
                print('Your answer is correct.')
                correct_ans = correct_ans + 1
            else:
                print('Your answer is wrong!')
        end_time = time.time()
        print('You answered ' + str(correct_ans) + ' questions correctly.')
        print('You answered in {0:0.1f} seconds'.format(end_time - start_time))


new_game = ArithmeticGame(2)
new_game.play_game()