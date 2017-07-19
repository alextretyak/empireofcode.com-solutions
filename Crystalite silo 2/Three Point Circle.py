import math

def circle_equation_(note):
    (Ax, Ay), (Bx, By), (Cx, Cy) = eval(note)
    Bx += .0001
    By += .0001
    aSlope = (By - Ay)/(Bx - Ax)
    bSlope = (Cy - By)/(Cx - Bx)  
    centerx = (aSlope*bSlope*(Ay - Cy) + bSlope*(Ax + Bx)
        - aSlope*(Bx+Cx) )/(2* (bSlope-aSlope) )
    centery = -1*(centerx - (Ax+Bx)/2)/aSlope +  (Ay+By)/2
    r = math.sqrt((centerx-Ax)**2 + (centery-Ay)**2)
    def l(x):
        r = str(round(x, 2))
        return r[:-2] if r.endswith(".0") else r
    return "(x-"+l(centerx)+")^2+(y-"+l(centery)+")^2="+l(r)+"^2"
    
def circle_equation(note):
    (Ax, Ay), (Bx, By), (Cx, Cy) = eval(note)
    
    offset = Bx**2 + By**2
    bc =   ( Ax**2 + Ay**2 - offset )/2.0
    cd =   (offset - Cx**2 - Cy**2)/2.0
    det =  (Ax - Bx) * (By - Cy) - (Bx - Cx)* (Ay - By)
    idet = 1/det
    centerx =  (bc * (By - Cy) - cd * (Ay - By)) * idet
    centery =  (cd * (Ax - Bx) - bc * (Bx - Cx)) * idet

    r = math.sqrt((centerx-Ax)**2 + (centery-Ay)**2)
    def l(x):
        r = str(round(x, 2))
        return r[:-2] if r.endswith(".0") else r
    return "(x-"+l(centerx)+")^2+(y-"+l(centery)+")^2="+l(r)+"^2"

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert circle_equation("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert circle_equation("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

    print("Use 'Check' to earn sweet rewards!")
