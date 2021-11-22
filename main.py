import os
os.environ['KIVY_HOME'] = 'DeckMaster'
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty,NumericProperty
#eee7b366-d9c1-4dc2-ac5c-ad177c4a18da

test_string = ["item","item2","item3"]
Builder.load_string("""

<Test>:
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False
    tab_width: 130

    TabbedPanelItem:
        text: 'Card Sets'
        Label:
            text: 'Select stuff'
    TabbedPanelItem:
        text: 'Deck Builder'
        GridLayout:
            cols:2
            padding:[5,10,5,10]
            spacing:[10,10]
            row_force_default:True
            row_default_height:50
            Button:
                text: 'Create new deck'
                size_hint_x:None
                width:120
            Label:
                text: 'Create a new non-standard deck (any set)'
            Button:
                text: 'Create new deck'
                size_hint_x:None
                width:120
            Label:
                text: 'Create a new standard deck (***current sets only***)'
    TabbedPanelItem:
        text: 'Deck List'
        RstDocument:
            text:
                '\\n'.join(("Complete list", "------------",
                "Summary view."))



""")

class Test(TabbedPanel):
    pass

class DeckManagerApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    DeckManagerApp().run()