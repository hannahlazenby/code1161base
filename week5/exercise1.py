# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
import math


# return a lit of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Return a list of countdown messages."""
    countdown_message = []
    start = int(start)
    stop = int(stop)
    if stop < start:
        x = -1
    else:
        x = 1
    for i in range(start, stop, x):
        countdown_message.append(message)
    countdown_message.append(completion_message)
    return countdown_message


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Calculate the hypotenuse of a triangle."""
    hypotenuse = math.sqrt(math.pow(base, 2) + math.pow(height, 2))
    return hypotenuse


def calculate_area(base, height):
    """Calculate the area of the triangle."""
    area = base * height * 1/2
    return area


def calculate_perimeter(base, height):
    """Calculate the perimeter of a triagle."""
    perimeter = calculate_hypotenuse(base, height) + base + height
    return perimeter


def calculate_aspect(base, height):
    """Calculate the aspect ratio of a triangle."""
    if base < height:
        return "tall"
    elif base > height:
        return "wide"
    elif base == height:
        return "equal"


def get_triangle_facts(base, height, units="mm"):
    """Get traingle facts from its base and height."""
    area = calculate_area(base, height)
    perimeter = calculate_perimeter(base, height)
    hypotenuse = calculate_hypotenuse(base, height)
    aspect = calculate_aspect(base, height)
    return {"area": area,
            "perimeter": perimeter,
            "height": height,
            "base": base,
            "hypotenuse": hypotenuse,
            "aspect": aspect,
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Propertie of a triangle."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)
    aspect = facts_dictionary["aspect"]
    if aspect == "tall":
        diagram = tall.format(**facts_dictionary)
    elif aspect == "wide":
        diagram = wide.format(**facts_dictionary)
    elif aspect == "equal":
        diagram = equal.format(**facts_dictionary)
    return diagram
    return facts


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Triangle Master."""
    facts = get_triangle_facts(base, height)
    diagram = tell_me_about_this_right_triangle(facts)
    if return_diagram and return_dictionary:
        return {"facts": facts, "diagram": diagram}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return {"facts": facts}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Create a word pyramid."""
    pyramid_list = []
    list_of_lengths = []
    for i in range(3, 21, 2):
        list_of_lengths.append(int(i))
    for i in range(20, 3, -2):
        list_of_lengths.append(int(i))
    pyramid_list = list_of_words_with_lengths(list_of_lengths)
    return pyramid_list


def get_a_word_of_length_n(length):
    """Get random word with specific length."""
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    try:
        if length >= 3:
            if type(length) is int:
                url = baseURL + str(length)
                r = requests.get(url)
                message = r.text
                return message
    except:
        None


def list_of_words_with_lengths(list_of_lengths):
    """Create a list of words with various lengths."""
    pyramid_list = []
    for x in list_of_lengths:
        pyramid_list.append(get_a_word_of_length_n(x))
    return pyramid_list
