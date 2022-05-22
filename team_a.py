# jefcolbi
# franckmario
# monkey_king

"""
A Box in a Box

Given a pair of rectangles, determine whether one of the rectangles is completely contained within the other rectangle. You will be given each rectangles top-left coordinate in an x/y plane, the rectangle's width, and the rectangle's height. One rectangle is "completely contained" by a rectangle that completely covers it, if viewed from above the plane. This puzzle should be solved using an Object-Oriented approach.
Business Rules/Errata

    * Data Structure Required: Rectangle You should produce and compare Rectangle objects in your solution, not the raw rectangle measurements.
    * The rectangle dimensions will be given in an array, in the format [(top left x coordinate), (top left y coordinate), (width), (height)].
    * Your function should take two Rectangle objects as arguments.
    * The units of width and height are irrelevant and can be ignored.
    * The coordinate system for this challenge is 2-dimensional, with x increasing from left to right, and y increasing from top to bottom.

    * Your final result should include a function that, given two sets of rectangle dimensions, returns a boolean value,
    * Your function should return false if the two rectangles only partially overlap.


Une boîte dans une boîte

Étant donné une paire de rectangles, déterminez si l'un des rectangles est entièrement contenu dans l'autre rectangle. Vous recevrez chaque coordonnée en haut à gauche des rectangles dans un plan x/y, la largeur du rectangle et la hauteur du rectangle. Un rectangle est "complètement contenu" par un rectangle qui le recouvre complètement, s'il est vu du dessus du plan. Ce puzzle doit être résolu en utilisant une approche orientée objet.
Règles métier/Errata

    * Structure de données requise : Rectangle Vous devez produire et comparer des objets Rectangle dans votre solution, et non les mesures brutes du rectangle.
    * Les dimensions du rectangle seront données dans un tableau, au format [(coordonnée x en haut à gauche), (coordonnée en y en haut à gauche), (largeur), (hauteur)].
    * Votre fonction doit prendre deux objets Rectangle comme arguments.
    * Les unités de largeur et de hauteur ne sont pas pertinentes et peuvent être ignorées.
    * Le système de coordonnées pour ce défi est bidimensionnel, avec x augmentant de gauche à droite et y augmentant de haut en bas.
    * Votre résultat final doit inclure une fonction qui, étant donné deux ensembles de dimensions de rectangle, renvoie une valeur booléenne,
    * Votre fonction doit retourner false si les deux rectangles ne se chevauchent que partiellement.


const { Rectangle, rectanglesOverlap } = require('./solution');

test('Two rectangles that do not overlap', () => {
    var rectangle1 = new Rectangle(1, 4, 3, 3);
    var rectangle2 = new Rectangle(0, 3, 2, 1);
    expect(rectanglesOverlap(rectangle1, rectangle2)).toBe(false);
});

test('Two rectangles that DO overlap', () => {
    var rectangle1 = new Rectangle(1, 4, 3, 3);
    var rectangle2 = new Rectangle(0, 3, 4, 4);
    expect(rectanglesOverlap(rectangle1, rectangle2)).toBe(true);
});

test('Two rectangles that partially overlap', () => {
    var rectangle1 = new Rectangle(1, 4, 3, 3);
    var rectangle2 = new Rectangle(0, 3, 3, 3);
    expect(rectanglesOverlap(rectangle1, rectangle2)).toBe(false);
});


"""
print("code equipe A")

import unittest

class Rectangle(object):
    def __init__(self, coords:list):
        self.x_top_left = coords[0]
        self.y_top_left = coords[1]
        self.width = coords[2]
        self.height = coords[3]

    def __contains__(self, other):
        return self.contains(other)


    def contains(self, other):
    #return (self.x_top_left <= other.x_top_left <= self.x_top_left + self.width) and (self.y_top_left  <= other.y_top_left <= self.y_top_left  + self.height)  and self.width >= other.width and self.height >= other.height
        return (self.x_top_left <= other.x_top_left) and (other.x_top_left + other.width <= self.x_top_left + self.width) and (self.y_top_left  <= other.y_top_left) and (other.y_top_left + other.height <= self.y_top_left  + self.height)  and self.width >= other.width and self.height >= other.height


def rectangle_overlap(rect1: Rectangle, rect2: Rectangle)-> bool:
    return rect1.contains(rect2) or rect2.contains(rect1)



class TestRectangle(unittest.TestCase):
    def test_a(self):
        r1 = Rectangle([1, 4, 3, 3])
        r2 = Rectangle([0, 3, 2, 1])
        self.assertFalse(rectangle_overlap(r2, r1))

    def test_b(self):
        r1 = Rectangle([1, 4, 3, 3])
        r2 = Rectangle([0, 3, 4, 4])
        self.assertTrue(rectangle_overlap(r2, r1))

    def test_c(self):
        """
        
        """
        r1 = Rectangle([1, 4, 3, 3])
        r2 = Rectangle([0, 3, 3, 3])
        self.assertFalse(rectangle_overlap(r2, r1))

    def test_d(self):
        r1 = Rectangle([1, 4, 3, 3])
        r2 = Rectangle([0, 3, 3, 3])
        self.assertFalse(r1 in r2)


unittest.main()