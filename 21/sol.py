from collections import defaultdict
from functools import reduce
def to_image(s):
    return tuple(s.split('/'))

def parse(line):
    inp, outp = line.split(" => ")
    return to_image(inp), to_image(outp)

def rotate2(image):
    return (image[0][1] + image[1][1],
            image[0][0] + image[1][0])

def flip(image):
    return image[::-1]

def rotate3(image):
    return (image[0][2] + image[1][2] + image[2][2],
            image[0][1] + image[1][1] + image[2][1],
            image[0][0] + image[1][0] + image[2][0])

def find_match(image, lut):
    rotate = rotate2 if len(image) == 2 else rotate3
    for i in range(4):
        if image in lut:
            return lut[image]
        image = rotate(image)

    image = flip(image)
    for i in range(4):
        if image in lut:
            return lut[image]
        image = rotate(image)
    pdb.set_trace()

def enhance(image, lut):
    if len(image) % 2 == 0:
        rtrn = ['']*round(len(image)/2*3)
        for y in range(0, len(image), 2):
            oy = int(y/2*3)
            for x in range(0, len(image), 2):
                sub_image = tuple(s[x:x+2] for s in image[y:y+2])
                sub_image = find_match(sub_image, lut)
                rtrn[oy+0] += sub_image[0]
                rtrn[oy+1] += sub_image[1]
                rtrn[oy+2] += sub_image[2]
    else:
        rtrn = ['']*int(len(image)/3*4)
        for y in range(0, len(image), 3):
            oy = int(y/3*4)
            for x in range(0, len(image), 3):
                sub_image = tuple(s[x:x+3] for s in image[y:y+3])
                sub_image = find_match(sub_image, lut)
                rtrn[oy+0] += sub_image[0]
                rtrn[oy+1] += sub_image[1]
                rtrn[oy+2] += sub_image[2]
                rtrn[oy+3] += sub_image[3]
    return tuple(rtrn)


assert rotate2(to_image('../.#')) == to_image('.#/..')
assert rotate3(to_image('#../#.#/##.')) == to_image('.#./..#/###')

test_images = map(parse, ['../.# => ##./#../...', '.#./..#/### => #..#/..../..../#..#'])
test_lut = {inp: outp for inp, outp in test_images}
assert enhance(to_image('.#./..#/###'), test_lut) == to_image("#..#/..../..../#..#")

with open('input', 'r') as fp:
    images = (parse(line.strip('\n')) for line in fp)
    image_lut = {inp: outp for inp, outp in images}
    image = to_image('.#./..#/###')
    for i in range(5): image = enhance(image, image_lut)
    print("pt1: {}".format(sum(row.count('#') for row in image)))

    for i in range(13): image = enhance(image, image_lut)
    print("pt2: {}".format(sum(row.count('#') for row in image)))
