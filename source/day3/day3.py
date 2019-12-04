#part 1
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.distance = abs(x)+abs(y)



    def toString(self):
        return "("+str(self.x)+","+str(self.y)+")"

class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        if p1.x == p2.x:
            self.direction = 'y'
        elif p1.y == p2.y:
            self.direction = 'x'
        else: 
            self.direction = 'error'

        self.minX = min([p1.x, p2.x])
        self.maxX = max([p1.x, p2.x])

        self.minY = min([p1.y, p2.y])
        self.maxY = max([p1.y, p2.y])

        self.length = maxX-minX + maxY-minY

    def intersects(self, other):
        # parallels don't intersect
        if self.direction == other.direction:
            return False, Point()

        # sort by min x
        if self.minX > other.minX:
            left = other
            right = self
        else:
            left = self
            right = other

        # if min x of 'right' line is greater than max x of 'left' line
        # then the two are not intersecting
        if right.minX > left.maxX:
            return False, Point()

        # sort by min y
        if self.minY > other.minY:
            lower = other
            upper = self
        else:
            lower = self
            upper = other
        
        # if min y of 'upper' line is greater than max y of 'lower' line
        # then the two are not intersecting
        if upper.minY > lower.maxY:
            return False, Point()

        # if both x and y indicate intersection, it's an intersection
        return True, Point(lower.minX, upper.maxY)
        
import copy
def convertToPointList(wire):
    res = []
    
    p = Point()
    res.append(Point())

    for string in wire:
        dir = string[0]
        amnt = int(string[1:])

        if dir == 'R':
            p.x += amnt
        elif dir == 'L':
            p.x -= amnt
        elif dir == 'D':
            p.y -= amnt
        elif dir == 'U':
            p.y += amnt
        else:
            exit()

        res.append(copy.deepcopy(p))
        
    return res

def createLineSegments(pointList):
    res = []
    p1 = Point()

    iterpointList = iter(pointList)
    next(iterpointList)
    for point in iterpointList:
        res.append(LineSegment(p1, point))
        p1 = point

    return res

def getIntersections(lsList1, lsList2):
    res = []
    for ls in lsList1:
        for ls2 in lsList2:
            intersects, intersection = ls.intersects(ls2)
            if intersects == True:
                res.append(intersection)
    return res

def dissassembleBothWires(wires):
    if len(wires) != 2:
        exit()

    lslist1 = createLineSegments(convertToPointList(wires[0]))
    lslist2 = createLineSegments(convertToPointList(wires[1]))

    return lslist1, lslist2

import operator
def getNearestIntersection(wires):
    lslist1, lslist2 = dissassembleBothWires(wires)

    intersections = getIntersections(lslist1, lslist2)
    intersections.sort(key=operator.attrgetter('distance'))
    print("Found", len(intersections), "intersections")
    return intersections[0]

def getIntersectionsAndDistance(lsList1, lsList2):
    res = []
    for ls in lsList1:
        for ls2 in lsList2:

            intersects, intersection = ls.intersects(ls2)
            if intersects == True:
                res.append(intersection)
    return res

def getFirstIntersection(wires):
    lslist1, lslist2 = dissassembleBothWires(wires)
    intersectionsSortedByList1 = getIntersections(lslist2, lslist1)
    intersectionsSortedByList2 = getIntersections(lslist1, lslist2)

#part 2