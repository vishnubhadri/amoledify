import os
import pytest
import numpy as np
from PIL import Image
import src.amoledify as amoledify

import time

current_time = str(time.time())

def assert_images_equal(image_1: str, image_2: str):
    global current_time
    img1 = Image.open(image_1)
    img2 = Image.open(image_2)

    # Convert to same mode and size for comparison
    img2 = img2.convert(img1.mode)
    img2 = img2.resize(img1.size)

    sum_sq_diff = np.sum((np.asarray(img1).astype('float') - np.asarray(img2).astype('float'))**2)

    if sum_sq_diff == 0:
        # Images are exactly the same
        pass
    else:
        normalized_sum_sq_diff = sum_sq_diff / np.sqrt(sum_sq_diff)
        assert normalized_sum_sq_diff < 0.001



def test_answer():
    amoledify.main("amoledify.py -i ./images/white.png -o ./images/white-test-"+current_time+".png -c (255,255,255)")
    assert_images_equal("./baseline_images/{}.png", "./images/white-test-"+current_time+".png")
    
    amoledify.main("amoledify.py -i ./images/black.png -o ./images/black-test-"+current_time+".png")
    assert_images_equal("./baseline_images/black", "./images/black-test-"+current_time+".jpg")

    amoledify.main("amoledify.py -i ./images/test.jpg -o ./images/test-363636-"+current_time+".jpg -c (36,36,36)")
    assert_images_equal("./baseline_images/test-363636-32", "./images/test-363636-"+current_time+".jpg")

    amoledify.main("amoledify.py -i ./images/test.jpg -o ./images/test-222021-"+current_time+".jpg -c (22,20,21)")
    assert_images_equal("./baseline_images/test-222021-32", "./images/test-222021-"+current_time+".jpg")

    amoledify.main("amoledify.py -i ./images/test.jpg -o ./images/test-255255255-0-"+current_time+".jpg -c (22,20,21) -t 255")
    assert_images_equal("./baseline_images/test-255255255-0", "./images/test-255255255-0-"+current_time+".jpg")

    pass
