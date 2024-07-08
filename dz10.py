# def is_palindrome(s):
#     cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
#     return cleaned_string == cleaned_string[::-1]
# input_string = input("Введіть рядок: ")
# if is_palindrome(input_string):
#     print("Рядок є паліндромом.")
# else:
#     print("Рядок не є паліндромом.")


# def change_reserved_words_to_uppercase(text, reserved_words):
#     words = text.split()  
#     modified_words = [word.upper() if word.lower() in reserved_words else word for word in words]
   
#     modified_text = ' '.join(modified_words)
#     return modified_text


# input_text = input("Введіть текст: ")


# reserved_words_input = input("Введіть зарезервовані слова через пробіл: ")
# reserved_words = reserved_words_input.lower().split()


# modified_text = change_reserved_words_to_uppercase(input_text, reserved_words)


# print("Змінений текст:", modified_text)
import re
def count_sentences(text):

    sentences = re.split(r'[.!?]', text)
 
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)


input_text = input("Введіть текст: ")

sentence_count = count_sentences(input_text)


print("Кількість речень у тексті:", sentence_count)