from game_package import quiz_num, riddle_game
from random import randint

RIDDLE_QUESTION = {
        "Сидит дед в сто шуб одет, кто его раздевает, тот слёзы проливает": ['лук', 'onion'],
        "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]
    }


if __name__ == '__main__':
    print(quiz_num.quiz_num_value(randint(1, 100))(5))
    print("\n" + ("=" * 30) + "\n")
    riddle_game.get_circle_riddles(RIDDLE_QUESTION)
    riddle_game.show_results()
