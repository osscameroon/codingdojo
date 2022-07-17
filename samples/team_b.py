# Team B:
# - Alex * 
# - darker
# - Kayra / 2
# - Sim / 

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

print("[-] Code team B.")
import unittest

class Coord:
  # x / y
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Rectangle:
  def __init__(self, coords: list):
    x_top_left, y_top_left, width, height = coords
    self.coord_left = Coord(x_top_left, y_top_left) # extreme left
    self.coord_right = Coord(width + x_top_left, y_top_left - height)  # extreme droite

  def collision(self, rect2) -> bool:
    # au dessus ou en bas
    if (
      self.coord_right.y >= rect2.coord_right.y or rect2.coord_right.y >= self.coord_left.y
    ):
      return False

    # de cote
    if (self.coord_left.x >= rect2.coord_right.x or rect2.coord_right.x >= self.coord_right.x):
      return False
    
    return True


def rectangle_overlap(rect1: Rectangle, rect2: Rectangle) -> bool:
  if (
    rect1.coord_left.x == rect1.coord_right.x or rect1.coord_left.y == rect1.coord_right.y or
    rect2.coord_left.x == rect2.coord_right.x or rect2.coord_left.y == rect2.coord_right.y
  ):
    return False

  return rect1.collision(rect2)


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
        r1 = Rectangle([1, 4, 3, 3])
        r2 = Rectangle([0, 3, 3, 3])
        self.assertFalse(rectangle_overlap(r2, r1))

unittest.main()

# x
#
#         y
#              x
#
#                        y r1 -> r2   -> r1 , r2 | r2, r1
#                           r2 -> r1
#
#
#  (x, y)-----------------------------(x + w, y)
#   |                                      |                         
#   |    (a, b)------------(a + w1, b)     |
#   |         |            |               |
#   |         |            |               |
#   | (a, b + h2)--------(a + w1, b + h2)  |
#   |                                      |
#   |                                      |
# (x, y + h)---------------------------(x + w, y + h)
#
