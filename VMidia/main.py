from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

while True:
    try:
        menu = input('Musica ou Video: ').lower()
        os.system('clear')

        match menu:
            case "musica":
                url = input('Url musica: ')
                os.system('clear')
                yt = YouTube(url, on_progress_callback=on_progress)
                print(f'''{yt.title}
MUSICA BAIXADA''')

                ys = yt.streams.get_audio_only()
                destino_musica = "/home/mrx/Músicas"                
                ys.download(output_path=destino_musica)

            case "video":
                url = input('Url video: ')
                os.system('clear')
                yt = YouTube(url, on_progress_callback=on_progress)
                print(f'''{yt.title}
VIDEO BAIXADO''')                
                
                ys = yt.streams.get_highest_resolution()
                destino_video = "/home/mrx/Vídeos"                
                ys.download(output_path=destino_video)

        parada = input('\nCONTINUA: ').lower()
        if parada == "s":
            os.system('clear')
            continue            
        elif parada == "n":
            break

    except Exception as e:
        print(f'Operação não executada {e}')


