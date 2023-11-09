

class Rectangle:

    # fusionner les formalisme ? genre x1,x2,x3,x4 + un param yolo/coco
    # rappel : yolo = x, y les coordonnées du point au centntre du rectangle + h,w. Valeur relative entre 0 et 1
    # coco : x1,y1 les coordonnées du point en haut à gauche. x2,y2 les coordonnées du point en bas à droite. Valeur absolue entre 0 et size.img
    def __init__(self, x, y, h, w, formalism='yolo'):
        self.x1 = x
        self.x2 = y
        self.x3 = h
        self.x4 = w
        self.formalism = formalism


    def change_dimension(self, x1, x2, x3, x4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4

# Prendre en compte les chgt de dimension à partir des différents corner, arretes + chgt de position du rectangle







    
    def __str__(self):
        if self.formalism=='yolo':
            return f"x=({self.x1},{self.x2})\nheight={self.x3}\nwidth={self.x4}"
        return f"x1=({self.x1},{self.x2})\nx2=({self.x3},{self.x4})"



# NOTE while grab => transparent ? permettrai de set constamment les dimension pdt qu'on le grab
# NOTE garder les anciennes positions pour ctrl+Z ?
