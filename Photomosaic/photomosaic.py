from PIL import Image
from os import listdir, path
from math import fabs

''' the actual tile size '''
tile_size = 20#10

''' 
the size of the thumbnail. can be different than the tile size. if different
the resulting image will be larger (or smaller) than the source
'''
thumb_size = 20#10

''' the size of a tile quadrant (if using the quad-point model) '''
small_size = tile_size / 2
image = "g.JPG"
 
''' output directory '''
work_dir = "./"

''' directory for storing intermediate thumbnails (normalized) '''
work_thumb_dir = "normimages/"

''' source thumbnails directory '''
thumb_dir = "images/"


width, height = 0, 0
color_map = {}
file_color_map = {}
detailed_file_color_map = {}

def find_largest():
    largest_area = 0
    largest_file = None
    for f in listdir(full_img_dir):
        try:
            h,w = Image.open(path.join(full_img_dir, f)).size
            area = h * w
            largest_area, largest_file = (area, f) if area > largest_area else (largest_area, largest_file)
        except:
            pass
        
    print 'largest file is \r\n%s' % path.join(full_img_dir, largest_file)
    return Image.open(path.join(full_img_dir, largest_file))
    

def avg_color (image):
    total_color = (0,0,0)
    total_count = 0;
    for count, color in image.getcolors(image.size[0] * image.size[1]):
        total_count += count
        total_color = (
                        total_color[0] + (count * color[0]), 
                        total_color[1] + (count * color[1]), 
                        total_color[2] + (count * color[2])
                        )
        
    return (total_color[0]/total_count, total_color[1]/total_count, total_color[2]/total_count)

def color_dif(color1, color2):
    return (fabs(color1[0] - color2[0]) + fabs(color1[1] - color2[1]) + fabs(color1[2] - color2[2]))

def find_closest(tile):
    color = avg_color(tile)
    distance = 0
    color_key = None
    for key in file_color_map.keys():
        new_dist = color_dif(color, file_color_map[key])
        if (new_dist < distance) or (color_key == None):
            color_key = key
            distance = new_dist
        if (distance == 0):
            return color_key
    
    return color_key
    
def average(lst):
    sum = 0
    for x in lst: sum += x
    return sum / len(lst)
    
def find_closest_quadrants(tile):
    distance = 0
    color_key = None
    
    tiles = { 
                0: avg_color(tile.crop((0, 0, small_size, small_size))),
                1: avg_color(tile.crop((0, small_size, small_size, small_size * 2))),
                2: avg_color(tile.crop((small_size, 0, small_size * 2, small_size))),
                3: avg_color(tile.crop((small_size, small_size, small_size * 2, small_size * 2)))
            }

    for key in detailed_file_color_map.keys():
        new_dist = average([color_dif(tiles[idx], detailed_file_color_map[key][idx]) for idx in range(4)])
        if (new_dist < distance) or (color_key == None):
            color_key = key
            distance = new_dist
        if (distance == 0):
            return color_key

    return color_key

def normalize_thumbs():
    for f in listdir(thumb_dir):
        img = Image.open(path.join(thumb_dir, f))
        h,w = img.size
        new_size = w if h > w else h
        newImg = img.crop((0, 0, h, h))
        newImg.resize((thumb_size,thumb_size)).save(path.join(work_thumb_dir, f))

def build_filemap():
    for f in listdir(thumb_dir):
        thumb_name = path.join(work_thumb_dir, f)
        thumb = Image.open(thumb_name)
        file_color_map[thumb_name] = avg_color(thumb)
        s = thumb.size[0]/2
        detailed_file_color_map[thumb_name] = [
                                                avg_color(thumb.crop((0, 0, s, s))),
                                                avg_color(thumb.crop((0, s, s, s * 2))),
                                                avg_color(thumb.crop((s, 0, s * 2, s))),
                                                avg_color(thumb.crop((s, s, s * 2, s * 2))),
                                              ]

#def process_main(locator, fname, image):
#    normalize_thumbs()
#    width, height = image.size
#    
#    build_filemap()
#    
#    res = ['<html><body><table cellpadding="0" cellspacing="0">']
#    for offset_y in [y*tile_size for y in range(height / tile_size)]:
#        line = ['<tr>']
#        for offset_x in [x*tile_size for x in range(width / tile_size)]:
#            thumb_file = locator(image.crop((offset_x, offset_y, offset_x + tile_size, offset_y + tile_size)))
#            line.append('<td><img width="%d" height="%d" src="' % (tile_size, tile_size))
#            line.append(thumb_file)
#            line.append('"/></td>')
#        line.append('</tr>')
#        res.append(''.join(line))
#        
#    res.append('</table></body></html>')
#            
#    out = open(path.join(work_dir, fname), 'w')
#    for line in res:
#        out.write(line)
#    
#    out.close()

def process_main(locator, fname, image):
    normalize_thumbs()
    width, height = image.size
    
    build_filemap()
    
    final_image = Image.new('RGB', (width, 0))
    for offset_y in [y*tile_size for y in range(height / tile_size)]:
        line_image = Image.new('RGB', (0, tile_size))
        for offset_x in [x*tile_size for x in range(width / tile_size)]:
            thumb_file = locator(image.crop((offset_x, offset_y, offset_x + tile_size, offset_y + tile_size)))
            thumb_file = Image.open(thumb_file)
            line_image = hmerge(line_image, thumb_file)
        final_image=vmerge(final_image, line_image)
        
            
    final_image.save(path.join(work_dir, fname))
    
def hmerge (imgLeft, imgRight):
        imgL = imgLeft#Image.open(imgLeft)
        imgR = imgRight#Image.open(imgRight)

        imgWidth = imgL.size[0] + imgR.size[0]
        #print imgL.size[1] , imgR.size[1]
        assert(imgL.size[1] == imgR.size[1])
        imgHeight = imgL.size[1]

        imgNew = Image.new('RGB', (imgWidth, imgHeight))

        imgNew.paste(imgL,(0,0))
        imgNew.paste(imgR,(imgL.size[0], 0))

        return imgNew
    
def vmerge (imgUp, imgDown):
        imgU = imgUp#Image.open(imgUp)
        imgD = imgDown#Image.open(imgDown)

        imgHeight = imgU.size[1] + imgD.size[1]
        assert(imgU.size[0] == imgD.size[0])
        imgWidth = imgU.size[0]

        imgNew = Image.new('RGB', (imgWidth, imgHeight))

        imgNew.paste(imgU,(0,0))
        imgNew.paste(imgD,(0, imgU.size[1]))

        return imgNew

print 'quadrants'
process_main(find_closest_quadrants, 'out2.jpg', Image.open('g.JPG'))






