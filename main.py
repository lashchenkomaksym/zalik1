file1 = 'zalik.txt'
word1 = input("Введіть слово, яке потрібно замінити: ")
word2 = input("Введіть слово, на яке потрібно замінити: ")

def replace_words(file1, word1, word2):
    try:
        with open(file1, 'r') as file:
            file1read = file.read()
        new_file1 = file1read.replace(word1, word2)

        with open(file1, 'w') as file:
            file.write(new_file1)

        print(f"Слово '{word1}' було замінено на '{word2}' у файлі {file1}")

    except:
        print(f"Файл {file1} не знайдено, або сталася помилка.")


replace_words(file1, word1, word2)
