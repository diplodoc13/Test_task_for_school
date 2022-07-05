'''
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, 
кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые 
имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". 
Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и вывести количество животных на каждую букву алфавита. 
Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....
'''

from string import ascii_uppercase
import requests
from bs4 import BeautifulSoup


'''
This function search animals which name in Russian language
Result will be a dictionary with key - letter of Russian alphabet 
and value - number of animals whitch name start on this letter
'''


def main():

    current_page = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    prefix = 'https://ru.wikipedia.org'
    current_letter = 'А'
    result = {}

    while current_page and not current_letter in ascii_uppercase[0]:
        current_page_request = requests.get(current_page)

        soup = BeautifulSoup(current_page_request.text, 'lxml')

        current_page_content = soup.find('div', id='mw-pages')
        current_page_animals = current_page_content.find_all(
            'div', class_='mw-category-group')

        for animal in current_page_animals:
            current_letter = animal.find('h3').text
            current_letter_animals_count = len(animal.find_all('li'))
            if current_letter in result:
                result[current_letter] += current_letter_animals_count
            elif current_letter in ascii_uppercase[0]:
                break
            else:
                result[current_letter] = current_letter_animals_count

        next_page = current_page_content.find('a', text='Следующая страница')
        if next_page:
            current_page = prefix + next_page['href']
        else:
            current_page = None

    for letter, count_of_animals in result.items():
        print(f'{letter}: {count_of_animals}')


if __name__ == "__main__":
    print('Waiting for result...')
    main()
