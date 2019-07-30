import os
import cv2


def get_frames(video, output_path, format):
    video = cv2.VideoCapture(video)
    success, image = video.read()
    count = 0

    while success:
        timestamp = round(video.get(cv2.CAP_PROP_POS_MSEC))
        secs = int((timestamp / 1000) % 60)
        mins = int((timestamp / 60000) % 60)
        hour = int((timestamp / 3600000) % 24)
        msec = timestamp - (1000 * (secs + (mins * 60) + (hour * 3600)))
        x = [str(hour), str(mins).zfill(2), str(secs).zfill(2), str(msec).zfill(3)]
        time = ";".join(x)

        cv2.imwrite(os.path.join(output_path, "frames", str(time) + ".{}".format(format)), image)

        # TODO: Implement custom framerate.
        count += 1000  # 1 gets every frame (count can be removed), 1000 gets one frame per second
        video.set(cv2.CAP_PROP_POS_MSEC, count)
        success, image = video.read()
