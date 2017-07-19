R = 6371
import re, math

def cartesian(geo):
    r = re.match(R"(\d+)°(\d+)′(\d+)″(N|S),? ?(\d+)°(\d+)′(\d+)″(W|E)", geo)
    phi = math.radians(int(r.group(1)) + int(r.group(2))/60 + int(r.group(3))/3600)
    if r.group(4) == 'S': phi = -phi
    lmb = math.radians(int(r.group(5)) + int(r.group(6))/60 + int(r.group(7))/3600)
    if r.group(8) == 'W': lmb = -lmb
    return math.cos(phi)*math.cos(lmb), math.cos(phi)*math.sin(lmb), math.sin(phi)

def distance(first, second):
    x1, y1, z1 = cartesian(first)
    x2, y2, z2 = cartesian(second)
    return math.acos(x1*x2 + y1*y2 + z1*z2) * R

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"

    print("All done? Earn rewards by using the 'Check' button!")
