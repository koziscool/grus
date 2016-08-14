
def generalFormOfLineByTwoPoints( x0, y0, x1, y1):
    l = y0 - y1
    m = x1 - x0
    n = (x0 - x1)*y0 + (y1 - y0)*x0
    return (l, m, n)

def polarityOfPointRelativeToLine(x, y, l, m, n):
    return l*x + m*y + n

def oppositeSideOfLine(x0, y0, x1, y1, l, m, n):
    if polarityOfPointRelativeToLine(x0, y0, l, m, n) * \
        polarityOfPointRelativeToLine(x1, y1, l, m, n) < 0:
            return True
    else:
        return False

def sameSideOfLine(x0, y0, x1, y1, l, m, n):
    if polarityOfPointRelativeToLine(x0, y0, l, m, n) * \
        polarityOfPointRelativeToLine(x1, y1, l, m, n) > 0:
            return True
    else:
        return False

def e184():
    circleRadius = 5
    interiorPoints = []
    for x in xrange(-circleRadius, circleRadius + 1):
        for y in xrange(-circleRadius, circleRadius + 1):
            if x**2 + y**2 < circleRadius**2:
                interiorPoints.append((x, y))

    print len(interiorPoints)
    # print interiorPoints

    numTrianglesContainingOrigin = 0

    for v0 in interiorPoints:
        for v1 in interiorPoints:
            if v0 == v1:
                break

            for v2 in interiorPoints:
                if v2 == v1 or v2 == v0:
                    break

                l1 = generalFormOfLineByTwoPoints(v2[0], v2[1], v0[0], v0[1])
                l2 = generalFormOfLineByTwoPoints( v1[0], v1[1], v2[0], v2[1])
                l3 = generalFormOfLineByTwoPoints( v1[0], v1[1], v0[0], v0[1])

                if sameSideOfLine(0, 0, v1[0], v1[1], l1[0], l1[1], l1[2]) and \
                    sameSideOfLine(0, 0, v0[0], v0[1], l2[0], l2[1], l2[2]) and \
                     sameSideOfLine(0, 0, v2[0], v2[1], l3[0], l3[1], l3[2]):
                        # print v0, v1, v2
                        numTrianglesContainingOrigin += 1

    return numTrianglesContainingOrigin


if __name__ == '__main__':
    print e184()
