from ball_tracking_system.nodes.camera import CameraNode


def map_coordinate_to_turtlesim_coordinates(x, y):
    new_x = (x / CameraNode.video_width) * 11.0
    new_y = ((CameraNode.video_height - y) / CameraNode.video_height) * 11.0
    return new_x, new_y
