import os
import cv2


def image_comparison(output_path, sensitivity):
    frames = []
    s = {'low': 0.9, 'normal': 0.8, 'high': 0.6}

    for file in os.listdir(os.path.join(output_path, "frames")):
        image = cv2.imread(os.path.join(output_path, "frames", str(file)), cv2.IMREAD_COLOR)
        histogram = cv2.calcHist([image], [0], None, [256], [0, 255])
        frames.append([str(file), image, histogram])

    cv2.imwrite(os.path.join(output_path, "keyframes", str(frames[0][0])), frames[0][1])
    for i in range(len(frames) - 2):
        if (cv2.compareHist(frames[i][2], frames[i + 1][2], cv2.HISTCMP_CORREL)) < s[sensitivity]:
            cv2.imwrite(os.path.join(output_path, "keyframes", frames[i + 1][0]), frames[i + 1][1])