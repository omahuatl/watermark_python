# import all the libraries,
# don't forget  pip install Pillow
# https://pillow.readthedocs.io/en/stable/
# https://www.geeksforgeeks.org/python-pillow-creating-a-watermark/

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys

class WaterMark():
    def __init__(self):
        # a simple image to initialize the variable and be able to test without upload a real image
        self.the_image=Image.new("1",(1,1))
        self.the_WaterMark=Image.new("1",(1,1))


    def read_file(self,file_name : str):
        try:
            self.the_image = Image.open(file_name)
        except:
            print(f"Error al abrir el archivo {file_name}")


    def show_image(self):
        # this open the photo viewer
        if self.the_image.info!={}:
            self.the_image.show()
            plt.imshow(self.the_image)
        else:
            print("Not image Uploaded")

    def show_watermark(self):
        # this open the photo viewer
        if self.the_WaterMark.info!={}:
            self.the_WaterMark.show()
            plt.imshow(self.the_WaterMark)
        else:
            print("Not image with WaterMark created")

    def calculate_wm_position(self):
        #calculate the watermark position
        size=self.the_image.size
        the_x=size[0]
        the_y=size[1]
        the_x=int(the_x*0.7)
        the_y=int(the_y*0.9)
        the_tuple=(the_x,the_y)
        return the_tuple


    def add_watermark(self,the_text):
        if self.the_image.info!={}:
            self.the_WaterMark = self.the_image.copy()

            draw = ImageDraw.Draw(self.the_WaterMark)
            # ("font type",font size)
            font = ImageFont.truetype("arial.ttf", 15)
            # add Watermark - 4 parameters
            # coordinates with (0,0) as the top left corner, they are pixels. Any pixels drawn outside of the image bounds will be discarded.
            # The text or watermark itself
            # color in RGB (255,255,255)-White color text  , (0,0,0)-black color text
            # font
            draw.text(self.calculate_wm_position(),the_text, (255, 255, 255), font=font)
            plt.subplot(1, 2, 2)
            plt.title("Image with WaterMark")
        else:
            print("Not image Uploaded")

    def save_watermark(self):
        split_name=self.the_image.filename.split(".")
        split_name[0]=split_name[0]+"_WM"
        new_name=split_name[0]+"."+split_name[1]

        self.the_WaterMark.save(new_name)


"""
# TODO add the name from the beggining

import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

"""