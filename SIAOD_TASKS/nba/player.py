class player:
    """ Класс описывающий игрока NBA """

    def __init__(self, height, wingspan, avg_points, avg_takes, avg_passes):
        """Конструктор класса игрока NBA"""
        self.height = height
        self.wingspan = wingspan
        self.avg_points = avg_points
        self.avg_takes = avg_takes
        self.avg_passes = avg_passes

    def get_player_category(self):
        """Метод возвращающий категорию объекта игрока"""
        top_half = 0
        count_goods = 0
        count_sgoods = 0
        green_unicorn = False
        # Проверка роста
        if (self.height >= 190) and (self.height <= 220):
            count_goods += 1
            if self.height > 205:
                top_half += 1
        elif self.height > 220:
            count_sgoods += 1
            green_unicorn = True
        # Проверка размаха рук
        if (self.wingspan >= 200) and (self.wingspan <= 250):
            count_goods += 1
            if self.wingspan > 225:
                top_half += 1
        elif self.wingspan > 250:
            count_sgoods += 1
            green_unicorn = True
        # Проверка среднего кол-ва очков
        if (self.avg_points >= 10) and (self.avg_points <= 20):
            count_goods += 1
            if self.avg_points > 15:
                top_half += 1
        elif self.avg_points > 20:
            count_sgoods += 1
        # Проверка среднего кол-ва подборов
        if (self.avg_takes >= 2) and (self.avg_takes <= 6):
            count_goods += 1
            if self.avg_takes > 4:
                top_half += 1
        elif self.avg_takes > 6:
            count_sgoods += 1
        # Проверка среднего кол-ва передач
        if (self.avg_passes >= 3) and (self.avg_passes <= 7):
            count_goods += 1
            if self.avg_passes > 4:
                top_half += 1
        elif self.avg_passes > 7:
            count_sgoods += 1

        # Выбор категории
        # Проверка на категорию 0
        if green_unicorn:
            if count_sgoods > 2:
                return 0
        # Проверка на категорию 1
        if ((count_sgoods > 1) and (top_half > 0)) or (((count_goods + count_sgoods) > 4) and ((count_sgoods + top_half) > 2)):
            return 1
        # Проверка на категорию 2
        if ((count_sgoods > 0) and (top_half > 0)) or (top_half > 2):
            return 2

        return 3
