import PIL
from PIL import Image
from PIL import ImageColor 
import random 

# importing things will help with loading and imaging

def read_lines_of_ints(text):
    “””Given a string with integers in it, return a list of those integers””"
    ints = []
    ints_as_strs = split_line(text)
    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints


    index = 0
    while index < len(ints_as_strs):
        int_as_str = ints_as_strs[index]
        ints.append(int(int_as_str))
        index += 1

    for int_as_str in ints_as_strs:    
        ints.append(int(int_as_str))
    return ints

def split_line(line):
    return line.split()


def read_file_into_list(filename):
   
 “””Given a filename, read that file and then convert it to a list of lists of ints. Example:
    We have a file with these contents:
    1 2
    3 4
    The return file would be  [[1,2,3,4]] “””

    “””given a file, return a list of each line in the file as a string”””
    with open(filename) as file:
        return file.readlines()


def test_can_read_line_of_ints():
    text = “10 12 9 345 2 78”
    assert read_line_of_ints(text) == [10 12 9 345 2 78]


#list_of_lists = []
#for line in lines:
#    list_of_lists.append(read_line_of_ints(line))
#return list_of_lists


class ElevationMap:
“”” a class that takes a matrix (list of lists, 2d)
of integers and can be used to generate an image of those evolution like a standard elevation map”””

def __int__(self, elevations):
    self.elevations = elevations

def elevations_at_coordinate(self, x, y):
    return self.evelations[y] [x]

def min_elevations(self):
    return min([
        min(row) for row in self.elevations])

def max_elevations(self):
    return max([max(row) for row in self.elevations])

def intensity_at_coordinate(self, x ,y):
    “””given an x, y coordinate, return the intensity level (used for grayscale in image) of the evolution at that coordinate.”””
elevation = self.elevation_at_coordinate_(x,y)

def draw_grayscale_gradient(self, filename, width, height):
    image = PIL.Image.new(mode=‘L’, size=(width, height) )
    for x in range(width):
        for y in range(height):
            image.putpixel((x,y))

list =[]


#0 -255 ; min - max value 
# black to white and find the min value. go through each line and add to the pervious. subtract the max from the min. 
# max-min = diff divide 


Class data

    def display_map(list):

  """ should change the data to an image if it works """
    
    # list = conv_to_rgb_values
    # im = Image.new("RGB", (600, 600))
    # for y, row in enumerate(conv_to_rgb_values):
    #     for x, value, in enumerate(row):
    #         im.putpixel((x, y), (value, value, value))
    #         im.putpixel((x, 300), (0, 0, 200))
    # im.save('map_image.png')
    # im.show('map_image.png')

print(display_map(list)

if __name__ = “__main__”:
    text = “10 12 9 345 2 78”
    read_line_of_ints(text)

print(read_file_into_ints(‘elevation_test.txt’))