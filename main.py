import os
os.environ['KIVY_HOME'] = 'DeckMaster'
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, NumericProperty, ObjectProperty, StringProperty
import setmanager
import search_tools
#eee7b366-d9c1-4dc2-ac5c-ad177c4a18da
# https://kivy.org/doc/stable/guide/events.html
#test_string = ["item","item2","item3"]

class Test(TabbedPanel):
    label_result = ObjectProperty()
    info = StringProperty()
    search_result = ListProperty()
    set_list = ListProperty()
    

    def get_search(self,val_txt):
        self.label_result.text = 'you are searching for {txt}'.format(txt=val_txt)
        set_list = setmanager.load_card_list()
        search_result = search_tools.name_search(set_list,val_txt)
        self.label_search.text = 'Search found {count} matches'.format(count = len(search_result))

    def set_list(self):
        setholder = setmanager.load_set_list()
        self.info = '''
        +-------------------------------+------------+----------------------------+
        |                    Title      | Set        | Subset                     |
        +===============================+============+============================+
        |                    body row 1 | column 2   | column 3-------------long  |
        +-------------------------------+------------+----------------------------+
        |                    body row 2 | column 2   | column 3-------------long  |
        +-------------------------------+------------+----------------------------+
        |                    body row 3 | column 2   | column 3-------------long  |
        +-------------------------------+------------+----------------------------+

        .. note::

            List may be malformed. Be careful::
        '''



class DeckManagerApp(App):
    def build(self):
        return Test(info='Active Set')

if __name__ == '__main__':
    DeckManagerApp().run()