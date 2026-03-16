import numpy as np
import cv2





def generate_frame(width, height, ball_pos, ball_radius):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.circle(
        frame,
        (int(ball_pos[0]), int(ball_pos[1])),
        ball_radius,
        (0, 0, 255),
        -1,
    )
    return frame 
