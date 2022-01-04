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
from kivy.properties import ListProperty, NumericProperty, ObjectProperty, StringProperty
import setmanager
#eee7b366-d9c1-4dc2-ac5c-ad177c4a18da

#test_string = ["item","item2","item3"]

class Test(TabbedPanel):
    label_result = ObjectProperty()
    info = StringProperty()
    

    def get_search(self,val_txt):
        self.label_result.text = 'you are searching for {txt}'.format(txt=val_txt)

    def set_list(self):
        setholder = setmanager.load_set_list()
        self.info = setholder[11]['name']



class DeckManagerApp(App):
    def build(self):
        return Test(info='Active Set')

if __name__ == '__main__':
    DeckManagerApp().run()