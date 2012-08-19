from abjad.tools.rhythmtreetools.ReducedAbjParser import ReducedAbjParser


def parse_reduced_ly_syntax(string):
    '''Parse the reduced LilyPond rhythmic syntax:

        >>> string = '4 -4. 8.. 5/3 { } 4'
        >>> result = rhythmtreetools.parse_reduced_ly_syntax(string)

    ::

        >>> for x in result:
        ...     x
        ...
        Note("c'4")
        Rest('r4.')
        Note("c'8..")
        Tuplet(5/3, [])
        Note("c'4")

    Return list.
    '''

    return ReducedAbjParser()(string)
