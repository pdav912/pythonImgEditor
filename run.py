from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image 
import cv2 
from functools import partial

class Back_end:
    def refresh_sub_menu(self):
        try:
            self.sub_menu.grid_forget()

        except:
            pass
        self.sub_menu = Frame(self.tools)
        self.sub_menu.grid(row=0, column=2, rowspan=9, padx=5, pady=5)

    def get_img(self):
        self.filename = filedialog.askopenfilename()
        self.image = cv2.imread(self.filename)
        self.editing_image = cv2.imread(self.filename)
        self.edited_image = cv2.imread(self.filename)


    def upload_action(self, img=None):
        self.canvas.delete("all")

        if img is None:
            self.get_img()
            img = self.editing_image

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channels = img.shape

        if height > 400:
            new_height = 400
            new_width = int(300 * (width/ height))

        else:
            new_width = 300
            new_height = int(400 * (height/ width))

        resize_img = cv2.resize(img, (new_width, new_height))
        resize_img = ImageTk.PhotoImage(Image.fromarray(resize_img))
        
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width/2, new_height/2, image=resize_img)

    def apply_effect(self, effect):
        if effect == "Negative":
            self.edited_image = cv2.cvtColor(self.editing_image, cv2.COLOR_BGR2GRAY)
            self.upload_action(self.edited_image)

        elif effect == "BW":
            gray_img = cv2.cvtColor(self.editing_image, cv2.COLOR_BGR2GRAY)
            (thresh, self.edited_image) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
            self.upload_action(self.edited_image)
            
        elif effect == "Sketch":
            print(effect)
        elif effect == "Emboss":
            print(effect)
        elif effect == "Sepia":
            print(effect)
        elif effect == "Binary":
            print(effect)
        elif effect == "Erosion":
            print(effect)
        elif effect == "Dilation":
            print(effect)


class Front_end(Back_end):
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x500")

        self.tools = Frame(self.root, width=500, height=400)
        self.tools.pack(padx=5, pady=5)
        self.tools.config(bg='#FFFAFA')

        self.canvas = Canvas(self.tools, background="gray", width=300, height=400)
        self.canvas.grid(row=0, column=1, rowspan=9, padx=5, pady= 15)

        self.sub_menu = Frame(self.tools)
        self.sub_menu.grid(row=0, column=2, rowspan=9, padx=5, pady=5)

        self.can_menu = Frame(self.root)
        self.can_menu.pack(padx=5, pady=5)

    def canvas_menu(self):
        self.apply_changes = Button(self.can_menu, text="Save")
        self.apply_changes.grid(row=0, column=1, padx=5, pady=5)

        self.revert_changes = Button(self.can_menu, text="Revert change")
        self.revert_changes.grid(row=0, column=2, padx=5, pady=5)
    
    def tool_menu(self): 
        self.upload_image = Button(self.tools, text="Upolad image", command=self.upload_action)
        self.upload_image.grid(row=0, column=0, padx=5, pady=5)

        self.crop = Button(self.tools, text="Crop", command=self.crop_image_action)
        self.crop.grid(row=1, column=0, padx=5, pady=5)

        self.add_text = Button(self.tools, text="Text", command=self.add_text_action)
        self.add_text.grid(row=2, column=0, padx=5, pady=5)

        self.draw = Button(self.tools, text="Draw", command=self.draw_action)
        self.draw.grid(row=3, column=0, padx=5, pady=5)

        self.filters = Button(self.tools, text="Filter", command=self.filters_action)
        self.filters.grid(row=4, column=0, padx=5, pady=5)

        self.blur_smooth = Button(self.tools, text="Blur/ Smooth", command=self.blur_smooth_action)
        self.blur_smooth.grid(row=5, column=0, padx=5, pady=5)

        self.brightness = Button(self.tools, text="Brightness", command=self.brightness_action)
        self.brightness.grid(row=6, column=0, padx=5, pady=5)

        self.rotate = Button(self.tools, text="Rotate", command=self.rotate_image_action)
        self.rotate.grid(row=7, column=0, padx=5, pady=5)

        self.flip = Button(self.tools, text="Flip", command=self.flip_image_action)
        self.flip.grid(row=8, column=0, padx=5, pady=5)

    def crop_image_action(self):
        self.refresh_sub_menu()
        self.crop_image_label = Label(self.sub_menu, text="crop image")
        self.crop_image_label.grid(row=0, column=0, pady=5, padx=5)

    def add_text_action(self):
        self.refresh_sub_menu()
        self.add_text_label = Label(self.sub_menu, text="Add text")
        self.add_text_label.grid(row=0, column=0, pady=5, padx=5)

        self.user_text = Entry(self.sub_menu)
        self.user_text.grid(row=1, column=0, pady=5, padx=5)

        self.font_colour = Button(self.sub_menu, text="Pick font colour")
        self.font_colour.grid(row=2, column=0, pady=5, padx=5)

    def draw_action(self):
        self.refresh_sub_menu()
        self.brush_colour = Button(self.sub_menu, text="Pick colour")
        self.brush_colour.grid(row=0, column=0, pady=5, padx=5)

    def filters_action(self):
        self.refresh_sub_menu()
        self.negative = Button(self.sub_menu, text="Negative", command=partial(self.apply_effect, effect="Negative"))
        self.negative.grid(row=0, column=0, pady=5, padx=5)

        self.black_and_white = Button(self.sub_menu, text="Black and white", command=partial(self.apply_effect, effect="BW"))
        self.black_and_white.grid(row=1, column=0, pady=5, padx=5)

        self.sketch_effect = Button(self.sub_menu, text="Sketch effect", command=partial(self.apply_effect, effect="Sketch"))
        self.sketch_effect.grid(row=2, column=0, pady=5, padx=5)

        self.emboss = Button(self.sub_menu, text="Emboss", command=partial(self.apply_effect, effect="Emboss"))
        self.emboss.grid(row=3, column=0, pady=5, padx=5)

        self.sepia = Button(self.sub_menu, text="Sepia", command=partial(self.apply_effect, effect="Sepia"))
        self.sepia.grid(row=4, column=0, pady=5, padx=5)

        self.binary_tresholding = Button(self.sub_menu, text="Binary thresholding", command=partial(self.apply_effect, effect="Binary"))
        self.binary_tresholding.grid(row=5, column=0, pady=5, padx=5)

        self.erosion = Button(self.sub_menu, text="Erosion", command=partial(self.apply_effect, effect="Erosion"))
        self.erosion.grid(row=6, column=0, pady=5, padx=5)

        self.dilation = Button(self.sub_menu, text="Dilation", command=partial(self.apply_effect, effect="Dilation"))
        self.dilation.grid(row=7, column=0, pady=5, padx=5)

    def blur_smooth_action(self):
        self.refresh_sub_menu()
        self.average_blur_label = Label(self.sub_menu, text="Average blur")
        self.average_blur_label.grid(row=0, column=0, pady=5, padx=5)

        self.average_blur_slider = Scale(self.sub_menu, from_=0, to=256, orient=HORIZONTAL)
        self.average_blur_slider.grid(row=1, column=0, pady=5, padx=5)

        self.gaussian_blur_label = Label(self.sub_menu, text="Gaussian blur")
        self.gaussian_blur_label.grid(row=2, column=0, pady=5, padx=5)

        self.gaussian_blur_slider = Scale(self.sub_menu, from_=0, to=256, orient=HORIZONTAL)
        self.gaussian_blur_slider.grid(row=3, column=0, pady=5, padx=5)

        self.median_blur_label = Label(self.sub_menu, text="Median blur")
        self.median_blur_label.grid(row=4, column=0, pady=5, padx=5)

        self.median_blur_slider = Scale(self.sub_menu, from_=0, to=256, orient=HORIZONTAL)
        self.median_blur_slider.grid(row=5, column=0, pady=5, padx=5)   

    def brightness_action(self):
        self.refresh_sub_menu()
        self.brightness_label = Label(self.sub_menu, text="brightness")
        self.brightness_label.grid(row=0, column=0, pady=5, padx=5)

        self.brightness_slider = Scale(self.sub_menu, from_=0, to=2, orient=HORIZONTAL)
        self.brightness_slider.grid(row=1, column=0, pady=5, padx=5)

        self.saturation_label = Label(self.sub_menu, text="Saturation")
        self.saturation_label.grid(row=2, column=0, pady=5, padx=5)

        self.saturation_slider = Scale(self.sub_menu, from_=0, to=2, orient=HORIZONTAL)
        self.saturation_slider.grid(row=3, column=0, pady=5, padx=5)

    def rotate_image_action(self):
        self.refresh_sub_menu()
        self.rotate_image_right = Button(self.sub_menu, text="Right")
        self.rotate_image_right.grid(row=0, column=0, pady=5, padx=5)

        self.rotate_image_left = Button(self.sub_menu, text="Left")
        self.rotate_image_left.grid(row=1, column=0, pady=5, padx=5)

    def flip_image_action(self):
        self.refresh_sub_menu()
        self.flip_image = Button(self.sub_menu, text="Flip")
        self.flip_image.grid(row=0, column=0, pady=5, padx=5)
                

class App(Front_end):
    def __init__(self, root):
        super().__init__(root)

    def build(self):
        self.tool_menu()
        self.canvas_menu()


root = Tk()
app = App(root)
app.build()
root.mainloop()