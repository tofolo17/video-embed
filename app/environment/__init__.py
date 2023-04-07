import os


class Args:
    def __init__(self):
        self.background_video = os.environ.get('BACKGROUND_FILE')
        self.caption_video = os.environ.get('CAPTION_FILE')
        self.output_video = os.environ.get('OUTPUT_FILE')
        self.output_video_size = os.environ.get('SIZE')


def check_content(args):
    """Check if there's a video in the input folder"""
    caption_video = args.caption_video
    background_video = args.background_video

    # docker/ é a root do container
    if caption_video in os.listdir(
        'app/input'
    ) and background_video in os.listdir('app/input'):
        return
    raise Exception('There is no video with these names in the input folder')
