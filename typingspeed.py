import time
import random
import string

def generate_random_text(difficulty):
    if difficulty == "easy":
        sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "Life is like a box of chocolates; you never know what you're gonna get.",
            "Success is not the key to happiness. Happiness is the key to success.",
            "In three words I can sum up everything I've learned about life: it goes on."
        ]
    elif difficulty == "medium":
        sentences = [
            "The only way to do great work is to love what you do.",
            "Be yourself; everyone else is already taken.",
            "The best preparation for tomorrow is doing your best today.",
            "Don't watch the clock; do what it does. Keep going.",
            "Believe you can and you're halfway there."
        ]
    elif difficulty == "hard":
        sentences = [
            "Life isn't about finding yourself. It's about creating yourself.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "It does not matter how slowly you go as long as you do not stop.",
            "The only limit to our realization of tomorrow will be our doubts of today.",
            "The secret of getting ahead is getting started."
        ]
    else:
        sentences = []

    random_sentence = random.choice(sentences)
    return random_sentence

def calculate_typing_speed(start_time, end_time, typed_text):
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    words = len(typed_text.split())
    speed = words / minutes
    return speed

def run_speed_typing_test():
    print("Speed Typing Test")
    print("Choose difficulty mode:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    mode = input("Enter the mode number (1-3): ")
    if mode == "1":
        difficulty = "easy"
    elif mode == "2":
        difficulty = "medium"
    elif mode == "3":
        difficulty = "hard"
    else:
        print("Invalid mode selected. Exiting...")
        return

    random_sentence = generate_random_text(difficulty)
    print("\nType the following sentence as fast as you can. Press Enter when you're done.\n")
    print(random_sentence + "\n")

    input("Press Enter to start the timer...")
    start_time = time.time()

    typed_text = input()

    end_time = time.time()

    speed = calculate_typing_speed(start_time, end_time, typed_text)

    print("\n--- Result ---")
    print("Typed Text:", typed_text)
    print("Elapsed Time: {:.2f} seconds".format(end_time - start_time))
    print("Typing Speed: {:.2f} words per minute".format(speed))

run_speed_typing_test()
