import re

from .mean_shift import MeanShiftTracker
from .cam_shift import CamShiftTracker

from .params import images_params


def main():
    image_number = int(input(
        "Choose image from list: \n{} \n".format(
            '\n'.join(["{}: {}".format(str(ix), image)
                       for ix, image in enumerate(images_params, 1)])
        )
    ))

    roi = input("Image ROI (coma_separated):")
    roi = list(map(int, re.findall(r"[\w']+", roi)))

    roi_default = [209, 90, 66, 125]
    image = list(images_params.items())[image_number][0]

    CamShiftTracker(image).track(roi=roi)
