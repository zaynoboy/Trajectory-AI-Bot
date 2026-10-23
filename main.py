
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.06, 0.12, 1)


class TrajectoryBot(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="[b]TRAJECTORY AI BOT[/b]",
            markup=True,
            font_size=25,
            size_hint_y=None,
            height=65
        ))

        layout.add_widget(Label(
            text="Analyse pédagogique des prix",
            font_size=16,
            size_hint_y=None,
            height=40
        ))

        self.price = TextInput(
            hint_text="Prix actuel (ex : 1.0850)",
            multiline=False,
            input_filter="float",
            font_size=20,
            size_hint_y=None,
            height=55
        )
        layout.add_widget(self.price)

        self.result = Label(
            text="Entre un prix pour commencer",
            font_size=18
        )
        layout.add_widget(self.result)

        button = Button(
            text="ANALYSER",
            size_hint_y=None,
            height=60
        )
        button.bind(on_press=self.analyze)
        layout.add_widget(button)

        layout.add_widget(Label(
            text="Signaux indicatifs uniquement. "
                 "Aucun gain n'est garanti.",
            font_size=13
        ))

        return layout

    def analyze(self, instance):
        try:
            price = float(self.price.text.strip())
            if price <= 0:
                raise ValueError

            self.result.text = (
                f"Prix saisi : {price:.5f}\n"
                "ATTENDRE : entre plusieurs prix "
                "pour analyser une tendance."
            )
        except ValueError:
            self.result.text = "Entre un prix valide et positif."


if __name__ == "__main__":
    TrajectoryBot().run()
