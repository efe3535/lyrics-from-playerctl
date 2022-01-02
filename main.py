from gi.repository import Playerctl, GLib
from gi.repository import Playerctl, GLib
from time import sleep
from os import system
import lyricsgenius 

genius = lyricsgenius.Genius()
player = Playerctl.Player()
not_shown = True

def on_metadata(player, metadata):
    global not_shown # Dışarıdaki not_shown değişkenini aktarıyoruz
    if 'xesam:artist' in metadata.keys() and 'xesam:title' in metadata.keys() and not_shown == True: # şarkı başlığı ve sanatçı ismi varsa ve bu yazı hiç gösterilmemişse.
        song = genius.search_song(metadata['xesam:title'],metadata['xesam:artist']) # Şarkıyı API'da ara.
        system(f"echo \"{song.lyrics}\" | less") # Bulunan şarkı sözlerini listele. Less komutu ekranı kaplamasını ve kaydırma özelliğini sağlıyor.
        not_shown = False # Bir kere gösterildiği için daha görünmesini istemiyoruz.
        exit(0)
player.connect('metadata', on_metadata) # Eğer bir şarkı çalınıyorsa on_metadata fonksiyonuna bağlan.


"""
---   GLib işlemleri
"""
main = GLib.MainLoop()
main.run()
