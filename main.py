"""
Case-study
Developer: Kosilov I.
"""
from random import choice
from typing import List, Dict
from re import compile


def clean_text(text: str) -> List[str]:
    """
    Очищает текст от "мусорных" символов
    """
    text = text.replace("\n", " ")
    r = compile('[^а-яА-Я .,!?:-]')
    text = r.sub("", text)
    return [word for word in text.split(" ") if word not in ['', ".", ",", '!', '?', ':', "-", " "]]


def get_links(words: List[str]) -> Dict[str, List[str]]:
    """
    Возращает словарь из "звеньев и связей"
    """
    links = {}
    for index, word in enumerate(words[:-1]):
        if word in links:
            links[word].append(words[index + 1])
        else:
            links[word] = [words[index + 1]]
    return links


def make_sentence(links: Dict[str, List[str]]) -> str:
    """
    Генерирует предложение.
    """
    start_words = [word for word in links if "А" <= word[0] <= "Я" and word[-1] not in [".", "!", "?"]]
    end_words = {word for word in links if word[-1] in [".", "!", "?"]}
    while True:
        sentence = [choice(start_words)]
        while sentence[-1] not in end_words:
            sentence.append(choice(links[sentence[-1]]))
        if 5 <= len(sentence) <= 20:
            break
    return " ".join(sentence)


def main():
    file_name = input("Введите название файла: ")
    number_sentences = int(input("Введите сколько предложений должно быть сгенирировано: "))
    with open(file_name) as file:
        text = clean_text(file.read())
    links = get_links(text)
    for _ in range(number_sentences):
        print(make_sentence(links))


if __name__ == "__main__":
    main()
