import cv2
import subprocess


def capture_videos(caption_video, background_video):
    """
    Capture both videos

    Args:
        caption_video(str): Path to the video with the caption
        background_video(str): Path to the video with the background

    Raises:
        Exception: If the videos could not be captured

    Returns:
        tuple: Tuple with the two video captures
    """
    caption_cap = cv2.VideoCapture('app/input/' + caption_video)
    background_cap = cv2.VideoCapture('app/input/' + background_video)
    return caption_cap, background_cap


def get_video_size(size):
    """
    Get the size of the output video

    Args:
        size(str): Size of the output video

    Raises:
        Exception: If the size is invalid

    Returns:
        tuple: Size of the output video
    """
    size = size.split('x')
    if len(size) != 2:
        raise Exception('Invalid output video size')

    return int(size[0]), int(size[1])


def set_video_writer(fps, size):
    """
    Create the video writer

    Args:
        fps(int): FPS of the output video
        size(tuple): Size of the output video

    Raises:
        Exception: If the video writer could not be created

    Returns:
        VideoWriter: Video writer
    """

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    vw = cv2.VideoWriter()
    if not vw.open('app/temp/' + 'output.mp4', fourcc, fps, size, True):
        raise Exception('Could not create the video writer')
    return vw


def compress_video():
    """
    Compress the output video

    Args:
        output_video(str): Path to the output video
    """
    # Changes the output video name

    try:
        # Compress the output video
        subprocess.check_call(
            [
                'ffmpeg',
                '-y',
                '-i',
                'app/temp/' + 'output.mp4',
                '-vcodec',
                'libx264',
                '-crf',
                '28',
                'app/temp/' + 'output_compressed.mp4',
            ]
        )

    except subprocess.CalledProcessError as e:
        raise Exception('Could not compress the video')
