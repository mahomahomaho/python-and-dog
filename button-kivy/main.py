import logging
from functools import partial
import socket

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

import config


class TreatButton(Widget):

    def __init__(self, *a, **kw):
        super(TreatButton, self).__init__(*a, **kw)
        Clock.schedule_interval(self.addot, 2)

    def treat(self):
        conn = None
        try:
            conn = socket.create_connection((config.dispenser_ip, config.dispenser_port), timeout=3)
            conn.sendall(b"treat\n\n")
            self.label.text = "SENT"
            Clock.schedule_once(partial(self.read_and_close, conn=conn))
        except Exception as e:
            logging.exception("in try treat")
            self.label.text = "error:%s" % e
            # Clock.schedule_once(self.clear, 3)
            if conn:
                conn.close()

    def read_and_close(self, dt, conn=None):
        try:
            self.label.text = conn.recv(1000).decode("utf-8")
        except Exception:
            pass
        finally:
            conn.close()

    def addot(self, dt):
        self.label.text += "."


class TreatButtonApp(App):
    pass


if __name__ == '__main__':
    TreatButtonApp().run()
