# 3d coordinate program
# written by Wesley Greer on 3/6/2026

# Write a distance function that will take two 3-dimensional coordinates (as input)
import math
def coordinate_distance(cord1,cord2):
    distance = math.sqrt((cord2[0] - cord1[0])**2 + (cord2[1] - cord1[1] )**2 + (cord1[2] - cord2[2])**2)
    return distance
#mainline that has the user enter the two tuples.
def main():
    print('Enter two 3-dimensional coordinates, and I will calculate the distance between them.')
    print('Please separate the elements with spaces, but no commas. (e.g. 12 4 20)')
# include try except to handle errors
    try:
        coordinate1 = input('Enter the first 3-dimensional coordinate: ')
        tuple1 = tuple(float(x) for x in coordinate1.split())
        coordinate2 = input('Enter the second 3-dimensional coordinate: ')
        tuple2 = tuple(float(x) for x in coordinate2.split())
# call the distance function and print distance
        distance = coordinate_distance(tuple1,tuple2)
        print(f'The distance between the coordinates is: {distance:.2f}')
    except ValueError:
        print('Error: Please make sure to separate the elements with spaces only, and be sure to only enter numbers.')
        exit()
    except IndexError:
        print('Error: Please make your coordinate has enough elements.')
        exit()

if __name__ == '__main__':
    main()
