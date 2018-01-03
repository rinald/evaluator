#!/usr/bin/python3
"""A simple calculator application."""

from evaluator import Expression

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class CalculatorWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculator")
        self.set_size_request(200, 50)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)

        self.entry = Gtk.Entry()
        vbox.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button()
        self.button.set_label("Evaluate")
        self.button.connect("clicked", self.on_evaluate_clicked)
        vbox.pack_start(self.button, True, True, 0)

    def on_evaluate_clicked(self, button):
        expression = self.entry.get_text()
        value = Expression(expression).evaluate()
        self.entry.set_text(str(value))

def main():
    window = CalculatorWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()