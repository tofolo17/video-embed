import cv2

import utils
import environment

# from time import sleep


def main(args):
    # Check the project structure vitals
    environment.check_content(args)

    # Capture both videos
    captionCap, backgroundCap = utils.capture_videos(
        args.caption_video, args.background_video
    )

    # Get the FPS of the background video
    fps = backgroundCap.get(cv2.CAP_PROP_FPS)

    # Get the size of the output video
    size = utils.get_video_size(args.output_video_size)

    # Create the video writer
    out = utils.set_video_writer(fps, size)

    while True:
        # Read the frames
        caption_ret, caption_frame = captionCap.read()
        background_ret, background_frame = backgroundCap.read()

        # Break if there are no more frames
        if not caption_ret:
            break
        if not background_ret:
            break

        # Resize both frames to the output video size
        background_frame, caption_frame = utils.resize_frames(
            background_frame, caption_frame, size
        )

        # Overlay the caption frame over the background frame
        overlayed = utils.overlay_frames(background_frame, caption_frame)

        # Write the frame to the output video
        out.write(overlayed)

    # Release the resources
    captionCap.release()
    backgroundCap.release()
    out.release()

    # Compress the output video
    utils.compress_video()

    # Add the audio from the caption video to the compressed video
    utils.add_audio(args.caption_video, args.output_video)

    # Finished
    print('Concluído!')


if __name__ == '__main__':
    # Parse the arguments
    args = environment.Args()

    # Call the main function with the parsed arguments
    main(args)
