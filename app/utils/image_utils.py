import cv2
import numpy as np


def resize_frames(backgroundFrame, captionFrame, size):
    """
    Resize both frames to the output video size

    Args:
        backgroundFrame(numpy.ndarray): Background frame
        captionFrame(numpy.ndarray): Caption frame
        size(tuple): Size of the output video

    Returns:
        tuple: Tuple with the resized frames
    """
    backgroundFrame = cv2.resize(backgroundFrame, size)
    captionFrame = cv2.resize(captionFrame, size)

    return backgroundFrame, captionFrame


# Chroma key: in LAB, the A channel separates green from magenta, so Otsu on it
# isolates the green screen from the caption (text/emoji).
def generate_threshold(captionFrame):
    """
    Generate the threshold

    Args:
        captionFrame(numpy.ndarray): Caption frame

    Returns:
        numpy.ndarray: Threshold
    """
    # Convert the frame to the LAB color space
    lab = cv2.cvtColor(captionFrame, cv2.COLOR_BGR2LAB)

    # Get the A channel
    a_channel = lab[:, :, 1]

    # Generate the threshold
    th = cv2.threshold(
        a_channel, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return th


def overlay_frames(backgroundFrame, captionFrame):
    # Generate the threshold
    th = generate_threshold(captionFrame)

    # Mask the caption frame
    masked = cv2.bitwise_and(captionFrame, captionFrame, mask=th)

    # Where the caption mask is empty (green screen), show the background
    # Overlay the caption frame over the background frame
    overlayed = np.where(masked == 0, backgroundFrame, masked)

    return overlayed
