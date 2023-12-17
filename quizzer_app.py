import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}, Answer: {self.answer}"

class Quizzer:
    def __init__(self):
        self.cards = []

    def add_card(self, question, answer):
        self.cards.append(Flashcard(question, answer))

    def delete_flashcard_menu(self):
        if not self.cards:
            print("No flashcards to delete.\n")
            return

        counter = 1
        for x in self.cards:
            print(f"{counter}. {x}")
            counter += 1

        print("\nWhich question do you want to delete? (Enter the number)")
        print("If you don't want to delete a question and want to go back, press Q\n")
        option = input("Enter your option: ").strip()

        if option.lower() == "q":
            return
        else:
            try:
                option_index = int(option) - 1
                if 0 <= option_index < len(self.cards):
                    del self.cards[option_index]
                    print("Flashcard deleted successfully.\n")
                else:
                    print("Invalid option, please enter a valid number.")
            except ValueError:
                print("Invalid input, please enter a number.")

    def quiz(self):
        if not self.cards:
            print("No flashcards to take a quiz.\n")
            return

        choice = input("Do you want to shuffle the cards? (yes/no) ").lower()
        cards_to_use = random.sample(self.cards, len(self.cards)) if choice == "yes" else self.cards

        correct_answer = 0
        incorrect_answer = 0
        for card in cards_to_use:
            print(card.question)
            user_answer = input("Your answer: ")
            if user_answer.lower() == card.answer.lower():
                print("Correct!\n")
                correct_answer += 1
            else:
                print(f"Wrong! The correct answer is: {card.answer}\n")
                incorrect_answer += 1

        print(f"Quiz finished! Your score: {correct_answer}/{len(cards_to_use)}")

    def true_or_false(self):
        if not self.cards:
            print("No flashcards available. Add flashcards first.\n")
            return
        choice = input("Do you want to shuffle the cards? (yes/no) ").lower()
        cards_to_use = random.sample(self.cards, len(self.cards)) if choice == "yes" else self.cards

        correct_answers = 0
        for card in cards_to_use:
            print(card.question)

            # Selecting a random answer from other flashcards
            random_answer = random.choice(self.cards).answer
            print(f"Answer: {random_answer}")

            user_input = input("Is this correct? (True/False) ").lower()

            # Checking if user's response is correct
            if user_input in ["true", "false"]:
                is_correct = (random_answer.lower() == card.answer.lower())
                user_is_correct = (user_input == "true")

                if user_is_correct == is_correct:
                    print("Correct!\n")
                    correct_answers += 1
                else:
                    print("Wrong!\n")
            else:
                print("Invalid input. Please answer 'True' or 'False'.\n")

        print(f"True or False quiz finished! Your score: {correct_answers}/{len(cards_to_use)}")

    def menu(self):
        while True:
            print("\nWhat would you like to do?")
            print("1. Add flashcard")
            print("2. Delete flashcard")
            print("3. Start quiz")
            print("4. True or False quiz")
            print("5. Display all flashcards")
            print("6. Edit flashcards")
            print("7. Exit\n")
            try:
                input_menu_item = int(input('Choose an option:\n'))
                if input_menu_item > 0 and input_menu_item <= 7:
                    return input_menu_item
                else:
                    print("Please enter a number between 1 and 7.\n")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def add_flashcard_menu(self):
        question = input("Enter the question for your flashcard:\n")
        answer = input("Enter the answer for your flashcard:\n")
        self.add_card(question, answer)

    def display_flashcards(self):
        if not self.cards:
            print("No flashcards to display.\n")
            return
        x = 1
        for card in self.cards:
            print(f"{x}. Question: {card.question} - Answer: {card.answer}\n")
            x += 1

    def edit_flashcard(self):
        if not self.cards:
            print("No flashcards to delete.\n")
            return

        counter = 1
        for x in self.cards:
            print(f"{counter}. {x}")
            counter += 1

        # Get user input for which flashcard to edit
        try:
            card_number = int(input("Enter the number of the flashcard you want to edit: "))
            if card_number < 1 or card_number > len(self.cards):
                print("Invalid flashcard number.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        # Adjust for zero-based indexing
        card_index = card_number - 1

        # Get user input for what to edit
        print("What would you like to edit?")
        print("1. Question")
        print("2. Answer")
        print("3. Both Question and Answer")
        choice = input("Enter your choice: ")

        # Edit based on user choice
        if choice == "1":
            new_question = input("Enter the new question: ")
            self.cards[card_index].question = new_question
        elif choice == "2":
            new_answer = input("Enter the new answer: ")
            self.cards[card_index].answer = new_answer
        elif choice == "3":
            new_question = input("Enter the new question: ")
            new_answer = input("Enter the new answer: ")
            self.cards[card_index].question = new_question
            self.cards[card_index].answer = new_answer

    def run(self):
        while True:
            menu_choice = self.menu()
            if menu_choice == 1:
                self.add_flashcard_menu()
            if menu_choice == 2:
                self.delete_flashcard_menu()
            elif menu_choice == 3:
                self.quiz()
            elif menu_choice == 4:
                self.true_or_false()
            elif menu_choice == 5:
                self.display_flashcards()
            elif menu_choice == 6:
                self.edit_flashcard()
            elif menu_choice == 7:
                print("Exiting...\n")
                break

quizzer = Quizzer()
quizzer.run()