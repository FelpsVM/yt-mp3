import yt_dlp
import os

def download_video_as_mp3(url, save_path, progress_hook=None):
    """
    Função para baixar um vídeo do YouTube como MP3.

    :param url: URL do vídeo.
    :param save_path: Caminho onde o áudio será salvo.
    :param progress_hook: Função de callback para exibir o progresso.
    """
    try:
        # Define as opções para o yt-dlp
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Define o nome e caminho do arquivo
            'format': 'bestaudio/best',  # Baixa somente o melhor áudio disponível
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',   # Extrai o áudio e converte para MP3
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [progress_hook] if progress_hook else []
        }

        # Usando yt-dlp para fazer o download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return {"status": "success", "message": f"Arquivo salvo em {save_path}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
