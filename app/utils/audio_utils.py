import subprocess


def add_audio(caption_video, output_video):
    """
    Adds the audio from the caption video to the compressed video

    :param caption_video: The caption video
    :param compressed_video: The compressed video
    :return: The final video

    :raises Exception: If there is an error while extracting the audio
    :raises Exception: If there is an error while adding the audio
    """
    try:
        command = [
            'ffmpeg',
            '-y',
            '-i',
            'app/input/' + caption_video,
            'app/temp/' + 'caption_audio.mp3',
        ]

        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        raise Exception('Erro ao extrair áudio')

    try:
        command = [
            'ffmpeg',
            '-y',
            '-i',
            'app/temp/' + 'output_compressed.mp4',
            '-i',
            'app/temp/' + 'caption_audio.mp3',
            '-c',
            'copy',
            '-map',
            '0:v:0',
            '-map',
            '1:a:0',
            'app/output/' + output_video,
        ]

        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        raise Exception('Erro ao adicionar áudio')
