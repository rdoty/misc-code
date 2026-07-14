"""
Alice lives on a lattice. The lattice consists of points that have integer
coordinates. One day Alice decided she wants to go for a walk. She starts
at lattice point A and goes straight to lattice point B. After reaching B,
she turns 90 degress to the right and moves straight in that direction.

What is the first lattice point that Alice will reach after the turn?

The points A and B have coordinates (ax, ay) and (bx, by) respectively.

Write a function:
def solution((ax, ay), (bx, by))
such that given two tuples, finds the coordinates of the first lattice
point that Alice will reach after turning right. It must return a tuple.

For example, given:
(-1, 3), (3, 1)

The function should return (2,-1)

Assume points in the range of -50,50
Assume A and B are distinct
"""

import math

def find_final_lattice_point(point_a:tuple, point_b:tuple) -> tuple:
    # Calculate the vector from start_location to direction
    original_vector = (point_b[0] - point_a[0], point_b[1] - point_a[1])

    # Rotate vector 90 degrees right (clockwise) -- (x, y) becomes (y, -x)
    rotated_vector = (original_vector[1], -original_vector[0])
    
    # The greatest common divisor of components will get smallest step
    gcd_rotated_vector = math.gcd(rotated_vector[0], rotated_vector[1])
    
    # Divide by GCD to find step to next lattice point
    step = (
        rotated_vector[0] // gcd_rotated_vector,
        rotated_vector[1] // gcd_rotated_vector
    ) 
    # Add the step to starting point b
    next_step = (point_b[0] + step[0], point_b[1] + step[1])
    return next_step


def test_find_final_lattice_point():
    test_data_list = [
        {"start": (-1,3), "towards":(3,1), "destination": (2,-1)},
        {"start": (2,2), "towards":(2,-3), "destination": (1,-3)},
    ]
    for count, test_data in enumerate(test_data_list):
        actual = find_final_lattice_point(test_data['start'], test_data['towards'])
        assert test_data['destination'] == actual, \
            f"Test #{count+1}: Expected: '{test_data['destination']}': Actual: '{actual}'"

    print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_find_final_lattice_point()  # run tests
