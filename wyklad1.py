#zad 1
#     return a % b
#
# if __name__ == '__main__':
#     print(reszta(10, 3))
#     print(reszta(20, 7))
#     print(reszta(15, 4))

#zad 2
# sentence = input("Sentence: ")
#
# screen_width = 80
# text_width = len(sentence)
# box_width = text_width + 6
# left_margin = (screen_width - box_width) // 2
#
# print()
# print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
# print(' ' * left_margin + '|' + ' ' * (box_width - 2) + '|')
# print(' ' * left_margin + '|  ' + sentence + '  |')
# print(' ' * left_margin + '|' + ' ' * (box_width - 2) + '|')
# print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')

# optymaliozacja zad 2
from shutil import get_terminal_size
from textwrap import wrap

def box_print(prompt="Sentence: "):
    sentence = input(prompt)

    screen_width = get_terminal_size(fallback=(80, 24)).columns
    max_content_width = max(1, screen_width - 6)
    lines = wrap(sentence, width=max_content_width) or [""]
    content_width = max(len(line) for line in lines)
    box_width = content_width + 6
    left_margin = max((screen_width - box_width) // 2, 0)
    pad = " " * left_margin

    horizontal = "+" + "-" * (box_width - 2) + "+"
    empty      = "|" + " " * (box_width - 2) + "|"

    print()
    print(pad + horizontal)
    print(pad + empty)
    for line in lines:
        inside = f"|  {line.ljust(content_width)}  |"
        print(pad + inside)
    print(pad + empty)
    print(pad + horizontal)

if __name__ == "__main__":
    box_print()
