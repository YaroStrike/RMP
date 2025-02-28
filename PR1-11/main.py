from kivy.lang import Builder
from kivymd.app import MDApp

class RockPaperScissorsApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # Светлая тема
        self.theme_cls.primary_palette = "Red"  # Палитра "Fuchsia"
        self.players_choices = [None, None, None]  # Храним выбор игроков
        self.current_player = 0  # Текущий игрок, который делает выбор
        return Builder.load_file('ui.kv')

    def set_choice(self, choice):
        # Сохраняем выбор текущего игрока
        self.players_choices[self.current_player] = choice
        # Обновляем статус
        self.update_status()
        # Переключаемся на следующего игрока
        self.current_player = (self.current_player + 1) % 3

    def update_status(self):
        # Формируем сообщение о текущем статусе выбора
        status = []
        for i, choice in enumerate(self.players_choices):
            if choice is None:
                status.append(f"Игрок {i + 1} выбирает...")
            else:
                status.append(f"Игрок {i + 1} выбрал: {choice}")
        # Обновляем текст Label
        self.root.ids.result_label.text = "\n".join(status)

    def show_result(self):
        # Проверяем, все ли игроки сделали выбор
        if None in self.players_choices:
            self.root.ids.result_label.text = "Не все игроки сделали выбор!"
            return

        # Логика определения победителя
        results = {
            ("Камень", "Ножницы"): "Камень побеждает",
            ("Ножницы", "Бумага"): "Ножницы побеждают",
            ("Бумага", "Камень"): "Бумага побеждает"
        }

        # Проверяем, есть ли ничья
        if self.players_choices[0] == self.players_choices[1] == self.players_choices[2]:
            self.root.ids.result_label.text = "Ничья!"
        else:
            # Определяем победителей и проигравших
            winners = []
            losers = []
            for i in range(3):
                is_winner = True
                for j in range(3):
                    if i != j:
                        if (self.players_choices[j], self.players_choices[i]) in results:
                            is_winner = False
                            break
                if is_winner:
                    winners.append(f"Игрок {i + 1}")
                else:
                    losers.append(f"Игрок {i + 1}")

            # Формируем итоговое сообщение
            if winners:
                winners_text = " и ".join(winners) + " побеждают!"
                losers_text = " и ".join(losers) + " проиграли." if losers else ""
                self.root.ids.result_label.text = winners_text + " " + losers_text
            else:
                self.root.ids.result_label.text = "Ничья!"

if __name__ == "__main__":
    RockPaperScissorsApp().run()