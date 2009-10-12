from abjad import *


def test_override_spanner___init___01( ):
   '''Five-argument form uses context specification.'''

   t = Staff(construct.scale(8))
   override = Override(t[:4], 'Staff', 'Beam', 'positions', (8, 8))

   r'''
   \new Staff {
           \override Staff.Beam #'positions = #'(8 . 8)
           c'8
           d'8
           e'8
           f'8
           \revert Staff.Beam #'positions
           g'8
           a'8
           b'8
           c''8
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\t\\override Staff.Beam #'positions = #'(8 . 8)\n\tc'8\n\td'8\n\te'8\n\tf'8\n\t\\revert Staff.Beam #'positions\n\tg'8\n\ta'8\n\tb'8\n\tc''8\n}"


def test_override_spanner___init___02( ):
   '''Four-argument form does not use context specification.'''

   t = Staff(construct.scale(8))
   override = Override(t[:4], 'Beam', 'positions', (8, 8))

   r'''
   \new Staff {
           \override Beam #'positions = #'(8 . 8)
           c'8
           d'8
           e'8
           f'8
           \revert Beam #'positions
           g'8
           a'8
           b'8
           c''8
   }
   '''

   assert check.wf(t)
   assert "\\new Staff {\n\t\\override Beam #'positions = #'(8 . 8)\n\tc'8\n\td'8\n\te'8\n\tf'8\n\t\\revert Beam #'positions\n\tg'8\n\ta'8\n\tb'8\n\tc''8\n}"
