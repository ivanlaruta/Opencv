import cv2
from clases.MyImages import MyImages


if __name__ == '__main__':

    imagen= MyImages("ufc","images/ufc.jpg","foto de personajes ufc","jpg")
    print(imagen)
    imagen.to_gray_scale()
    imagen.to_resize_halve()
    imagen.search_face()
    imagen.show_image()

    imagen2= MyImages("sandler","images/sandler.jpg","foto de adam sandler ","jpg")
    print(imagen2)
    imagen2.to_gray_scale()
    imagen2.to_resize_halve()
    imagen2.search_face()
    imagen2.show_image()

