'''animation format:
    (
        frame this applies to, ex: 5 // from 5th frame onward,
        phrase, ex: "hello" // phrase to set on the model
    )
'''
'''cam_path format:
    (
        (target_pos, ex: (0, 0), 0, ramp_char,ex: "linear"/"exp"),
        target_rot, ex: (0, 0), ramp_dur, ex: 5, //frames
        target_scale, ex: (1, 1)
    )
        phrase, ex: "hello" // phrase to set on the model
    )
'''
phrases = {
    0: "swamp",
    35: "forest",
    70: "desert",
}
cam_path = {
    0:  ((0, 0), (0,  0), (1, 1),        0, "linear"),
    30: ((0, 0), (20,20), (1, 1),       40,    "exp"),
    37: ((0, 0), (20,20), (5, 5),       40,    "exp"),
    70: ((0, 0), (0,  0), (0.1, 0.1),    5, "linear"),
}
cam = Cam(cam_path)
for f in num_frames:
    phrase = phrases.get(f)
    frames.append(gen_frame())
    cam.step()