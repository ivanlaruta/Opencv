import cv2


class MyImages:

    def __init__(self, nombre, ruta, descripcion, formato ):
        self.nombre = nombre
        self.ruta = ruta
        self.descripcion = descripcion
        self.formato = formato

    def __str__(self):
            return '''nombre : {}
ruta : {}
descripcion: {}
formato: {}''' \
                .format(self.nombre, self.ruta, self.descripcion, self.formato)

    def read_image(self):
        """Leer una ruta de imagen  y devolver objeto imagen"""
        if isinstance(self.ruta, str):
            img = cv2.imread(self.ruta)
            return img
        else:
            print("formato no valido")
            return None

    def save(self,name_img,img):
        """Guarda una imgaen en formato jpg """
        name_img = self.nombre+" - "+name_img + ".jpg"
        cv2.imwrite(name_img, img)


    def show_image(self):
        """desplegar imagen original"""
        cv2.imshow(self.nombre, self.read_image())
        cv2.waitKey(0)
        #cv2.destroyAllWindows()



    def to_gray_scale(self):
        """Devuleve imagen en blanco y negro"""
        gray_img = cv2.cvtColor(self.read_image(), cv2.COLOR_BGR2GRAY)
        self.save("GRAY", gray_img)


    def to_resize_halve(self):
        """Recibe un objeto imagen y devuleve la imagen a la mitad del tamaño"""
        resize_img = cv2.resize(self.read_image(), (int(self.read_image().shape[1] / 2), int(self.read_image().shape[0] / 2)))
        self.save("HALVE", resize_img)



    def search_face(self):
        """Recibe un objeto imagen y devuleve la imagen con un rectangulo en un rostro"""
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        gray_img = cv2.cvtColor(self.read_image(), cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)

        for x, y, w, h in faces:
            img_rectangle = cv2.rectangle(self.read_image(), (x, y), (x + w, y + h), (0, 255, 0), 3)

        self.save("FACE", img_rectangle)

