

# STEP-1 IMPORTING THE REQUIRED LIBRARY 
from spellchecker import SpellChecker 

# STEP -2 CREATING THE APP CLASS
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

# STEP -3 CORRECT THE TEXT 
    def correct_text(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word)

# STEP -4 RETURING THE CORRECTED TEXT
        return ' '.join(corrected_words)
    
# STEP-5 RUNNING THE APP

    def run(self):
        print("\n ---SPELL CHECKER---")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')
            
            if text.lower() == 'exit':
                print('Closing the program....')
                break
            corrected_text = self.correct_text(text)
            print(f'Corrected Text : {corrected_text}')

# STEP-6 RUNNING THE MAIN PROGRAM
if __name__ == "__main__":
    SpellCheckerApp().run()