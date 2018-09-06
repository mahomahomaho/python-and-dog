from kivy.app import App
from kivy.uix.widget import Widget
from plyer import wifi


class TreatButton(Widget):
    @classmethod
    def treat(cls):
        wifi.connect('dispenser', {'password': 'dispenser_pass'})


class TreatButtonApp(App):
    pass


if __name__ == '__main__':
    TreatButtonApp().run()
