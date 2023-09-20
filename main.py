# Importing standart function from random module
from random import randint


DEFAULT_ATTACK: int = 5  # Default value of attack
DEFAULT_DEFENCE: int = 10  # Default value of defence
DEFAULT_STAMINA: int = 80  # Default value of stamina


class Character:
    """Default class for all type of characters."""

    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)  # Constant for range of damage
    RANGE_VALUE_DEFENCE = (5, 10)  # Constant for range of defence
    # Specials default constant
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name) -> None:
        self.name = name

    def attack(self):
        """Method of attack."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный {value_attack}'

    def defence(self):
        """Method of defence."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона'

    def special(self):
        """Method of special."""
        return (f'{self.name} применил специальное умение '
                f'«{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}»')

    def __str__(self):
        """Method that return class name and info about it"""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Base class for warriors."""
    BRIEF_DESC_CHAR_CLASS = ('дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный.')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    """Base class for mages."""
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    """Base class for healers."""
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """Return string with chosen character class"""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choise: str = ''
    while approve_choise != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choise = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class

    def start_training(char_class):
        """
        Принимает на вход имя и класс персонажа.
        Возвращает сообщения о результатах цикла тренировки персонажа.
        """
        commands = {'attack': char_class.attack(),
                    'defence': char_class.defence(),
                    'special': char_class.special()
                    }
        while cmd != 'skip':
            training = input('Введите команду:')
            if training in commands:
                
        
