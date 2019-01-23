# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

def minus(v1, v0):
    return tuple(i - j for i, j in zip(v1, v0))

def get_vector(p1, p0):
        return tuple(i - j for i, j in zip(p1, p0)) 

def v_multiply(v1, v0):
    return (v1[1] * v0[2] - v1[2] * v0[1], 
            v1[2] * v0[0] - v1[0] * v0[2],
            v1[0] * v0[1] - v1[1] * v0[0]) 

def s_multiply(v1, v0):
    return tuple(i * j for i, j in zip(v1, v0))

def abs(v):
    return sum(i * i for i in v) ** 0.5

def check_coord(p):
    """
        Check if the point is 2D or 3D coordinate.
    """
    if len(p) == 2:
        return (p[0], p[1], 0)
    elif len(p) != 3:
        raise ValueError("The point should be (x, y) or (x, y, z)")
    return p 

class Triangle:

    def __init__(self, p1, p2, p3): 
        p1, p2, p3 = [check_coord(i) for i in [p1, p2, p3]] 
        self.v1 = get_vector(p1, p2)
        self.v2 = get_vector(p1, p3) 
        self.v3 = get_vector(p2, p3) 

    def square(self):
        return 0.5 * abs(v_multiply(self.v1, self.v2))

    def perimeter(self):
        return sum(map(abs, [self.v1, self.v2, self.v3]))

    def altitudes(self):
        alt = []
        S = self.square()
        for side in map(abs, (self.v1, self.v2, self.v3)):
            alt.append(2 * S / side)
        return alt 

"""
Example:
# 2D
In [161]: t = Triangle((2, 0), (0, 2), (0, 0))

In [162]: t.square()
Out[162]: 2.0

In [163]: t.perimeter()
Out[163]: 6.82842712474619

In [164]: t.altitudes()
Out[164]: [1.414213562373095, 2.0, 2.0]
---
# 3D
In [170]: t = Triangle((1, -1, 2), (5, -6, 2), (1, 3, -1))

In [171]: t.perimeter()
Out[171]: 21.69875437841985

In [172]: t.square()
Out[172]: 12.5

In [173]: t.altitudes()
Out[173]: [3.904344047215152, 5.0, 2.4282146558931603]

"""


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Eq_trapezoid:
    
    def if_plain(self, p1, p2, p3, p4):
        """
        Check if 4 points belong to one plain.
        vectors:
        v1 = p1 - p2
        v2 = p1 - p3
        v3 = p1 - p4
        should form a figure with zero volume:
        |v1_x  v1_y  v1_z|
        |v2_x  v2_y  v2_z| = 0
        |v3_x  v3_y  v3_z|
        """
        v1 = get_vector(p1, p2)
        v2 = get_vector(p1, p3)
        v3 = get_vector(p1, p4)
        v2xv3 = v_multiply(v2, v3)
        v1xv2xv3 = (v1[0] * v2xv3[0], - v1[1] * v2xv3[1],
                    v1[2] * v2xv3[2])
        V = abs(v1xv2xv3)
        return V == 0

    def if_eq_side(self, v1, v2, v3, v4):
        """
        Check if the figure has equal sides.
        """
        return (abs(v1) == abs(v3)) or (abs(v2) == abs(v4)) 

    def if_trapezoid(self, v1, v2, v3, v4):
        return (abs(v_multiply(v1, v3)) == 0) or \
               (abs(v_multiply(v2, v4)) == 0) 
        
    def __init__(self, p1, p2, p3, p4):
        p1, p2, p3, p4 = [check_coord(i) for i in \
                [p1, p2, p3, p4]]
        assert self.if_plain(p1, p2, p3, p4), \
                "Points form a pyramid, not a trapezoid"
        p_list = [p1, p2, p3, p4]
        def mean_div_4(p_list, i):
            return sum(p[i] for p in p_list) / 4 

        middle_point = (mean_div_4(p_list, 0), \
                        mean_div_4(p_list, 1), \
                        mean_div_4(p_list, 2))

        p1, p2, p3, p4 = sorted(p_list, \
                key = lambda x: abs(minus(middle_point, x)))

        """
        ......p1.....p2.......
        ......................
        ......................
        ..........m...........
        ......................
        ......................
        .p3...............p4..
        """

        v1 = get_vector(p1, p3)
        v2 = get_vector(p1, p4)
        if abs(v1) < abs(v2):
            p3, p4 = p4, p3
        
        """
        ......p1.....p2.......
        ......................
        ......................
        ..........m...........
        ......................
        ......................
        .p4...............p3..
        """


        v1 = get_vector(p1, p2)
        v2 = get_vector(p2, p3)
        v3 = get_vector(p3, p4)
        v4 = get_vector(p4, p1) 

        assert self.if_eq_side(v1, v2, v3, v4), \
                "No equal sides"
                
        assert self.if_trapezoid(v1, v2, v3, v4), \
                "Not trapezoid"


        self.v1, self.v2, self.v3, self.v4 = v1, v2, v3, v4
        self.p1, self.p2, self.p3, self.p4 = p1, p2, p3, p4

    def sides(self):
        return list(map(abs, [self.v1, self.v2, self.v3, self.v4]))

    def perimeter(self):
        return sum(self.sides())

    def square(self):
        p1, p2, p3, p4 = self.p1, self.p2, self.p3, self.p4
        return Triangle(p1, p2, p3).square() + Triangle(p2, p3, p4).square() 
            
"""
Examples:
# simple example 2D
In [77]: t = Eq_trapezoid((0,0), (2,4), (6,4), (8,0))                           

In [78]: t.square()                                                             
Out[78]: 24.0

In [79]: t.perimeter()                                                          
Out[79]: 20.94427190999916

In [80]: t.sides()                                                              
Out[80]: [4.0, 4.47213595499958, 8.0, 4.47213595499958]

# simple example 3D
In [41]: t = Eq_trapezoid((0,0,0), (2,4,0), (6,4,0), (8,0,0))                   

In [42]: t.square()                                                             
Out[42]: 24.0

In [43]: t.perimeter()                                                          
Out[43]: 20.94427190999916

In [44]: t.sides()                                                              
Out[44]: [4.0, 4.47213595499958, 8.0, 4.47213595499958]

# make trapezoid valumetric (again)
In [45]: t = Eq_trapezoid((0,0,0), (2,4,1), (6,4,0), (8,0,0))                   
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-45-f3f24472ff9d> in <module>
----> 1 t = Eq_trapezoid((0,0,0), (2,4,1), (6,4,0), (8,0,0))

~/Codes/Geekbrains/Python_lessons_basic/lesson06/home_work/hw06_easy.py in __init__(self, p1, p2, p3, p4)
    119     def __init__(self, p1, p2, p3, p4):
    120         assert self.if_plain(p1, p2, p3, p4), \
--> 121                 "Points form a pyramid, not a trapezoid"
    122         p_list = [p1, p2, p3, p4]
    123 

AssertionError: Points form a pyramid, not a trapezoid

# make sides not equal 
In [46]: t = Eq_trapezoid((0,0,0), (2,5,0), (6,4,0), (8,0,0))                   
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-46-e664446935c7> in <module>
----> 1 t = Eq_trapezoid((0,0,0), (2,5,0), (6,4,0), (8,0,0))

~/Codes/Geekbrains/Python_lessons_basic/lesson06/home_work/hw06_easy.py in __init__(self, p1, p2, p3, p4)
    164 
    165         assert self.if_eq_side(v1, v2, v3, v4), \
--> 166                 "No equal sides"
    167 
    168         assert self.if_trapezoid(v1, v2, v3, v4), \

AssertionError: No equal sides

# change sides 
In [50]: t = Eq_trapezoid((0,0,0), (6,4,0), (2,4,0), (8,0,0))                   

In [51]: t.square()                                                             
Out[51]: 24.0

In [52]: t.sides()                                                              
Out[52]: [4.0, 4.47213595499958, 8.0, 4.47213595499958]

In [53]: t.perimeter()                                                          
Out[53]: 20.94427190999916

"""
