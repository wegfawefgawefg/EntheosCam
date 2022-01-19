import os
from PIL import Image, ImageOps, ImageChops
import subprocess

from animation_toolkit import KeyFrame, Transform, Vec2, Animation

def zoom(img, zoom):
    x, y = im.width/2, im.height/2
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)

if __name__ == "__main__":
    keyframes = {
        20: KeyFrame(
                Transform(
                    pos=Vec2(50, 30),
                    rot=Vec2(45, 0),
                    scale=Vec2(2, 2)
                ),
                KeyFrame.Ease.EXPONENTIAL),
        70: KeyFrame(
                Transform(
                    pos=Vec2(-50, 80),
                    rot=Vec2(-45, 0),
                    scale=Vec2(0.6, 0.8)
                ),
                KeyFrame.Ease.EXPONENTIAL),
        100: KeyFrame(
            Transform(
                pos=Vec2(5, 3),
                rot=Vec2(20, 0),
                scale=Vec2(3, 0.5)
            ),
            KeyFrame.Ease.EXPONENTIAL),
    }
    anim = Animation(keyframes, length=100)

    impath = "/home/vega/Coding/EntheosCam/"
    im_name = "cat"
    ext = ".png"
    im = Image.open(os.path.join(impath, im_name + ext))
    for i, delta in enumerate(anim.deltas):
        pos, rot, scale = delta.pos, delta.rot, delta.scale
        im = im.rotate(rot.x, resample=Image.BICUBIC)
        im = zoom(im, 1+scale.x)
        im = ImageChops.offset(im, int(pos.x), int(pos.y))
        im.save(os.path.join(impath, "animation", str(i) + ext))
    subprocess.run(
        ["ffmpeg", "-f", "image2", "-i", os.path.join(impath, "animation", "%d" + ext), "-vcodec", "libx264", "-crf", "25", "-pix_fmt", "yuv420p", os.path.join("out.mp4")]
    )


    