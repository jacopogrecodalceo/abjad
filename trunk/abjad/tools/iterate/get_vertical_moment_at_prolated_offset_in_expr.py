from abjad.component import _Component
from abjad.tools.iterate.naive_forward_in_expr import naive_forward_in_expr


def get_vertical_moment_at_prolated_offset_in_expr(governor, prolated_offset):
   r'''.. versionadded:: 1.1.2
   
   Get vertical moment at `prolated_offset` in `governor`.

   ::

      abjad> score = Score([ ])
      abjad> score.append(Staff([FixedDurationTuplet((4, 8), leaftools.make_repeated_notes(3))]))
      abjad> piano_staff = PianoStaff([ ])
      abjad> piano_staff.append(Staff(leaftools.make_repeated_notes(2, Rational(1, 4))))
      abjad> piano_staff.append(Staff(leaftools.make_repeated_notes(4)))
      abjad> piano_staff[1].clef.forced = Clef('bass')
      abjad> score.append(piano_staff)
      abjad> pitchtools.diatonicize(list(reversed(score.leaves)))
      abjad> f(score)
      \new Score <<
              \new Staff {
                      \times 4/3 {
                              d''8
                              c''8
                              b'8
                      }
              }
              \new PianoStaff <<
                      \new Staff {
                              a'4
                              g'4
                      }
                      \new Staff {
                              \clef "bass"
                              f'8
                              e'8
                              d'8
                              c'8
                      }
              >>
      >>
      abjad> vertical_moment = iterate.get_vertical_moment_at_prolated_offset_in_expr(piano_staff, Rational(1, 8))
      abjad> vertical_moment.leaves
      (Note(a', 4), Note(e', 8))

   .. todo:: optimize without full-component traversal.

   .. versionchanged:: 1.1.2
      renamed ``iterate.get_vertical_moment_at_prolated_offset_in( )`` to
      ``iterate.get_vertical_moment_at_prolated_offset_in_expr( )``.
   '''
   from abjad.tools.verticalitytools.VerticalMoment import VerticalMoment

   governors = [ ]
   message = 'must be Abjad component or list or tuple of Abjad components.'
   if isinstance(governor, _Component):
      governors.append(governor)
   elif isinstance(governor, (list, tuple)):
      for x in governor:
         if isinstance(x, _Component):
            governors.append(x)
         else:
            raise TypeError(message)
   else:
      raise TypeError(message)
   governors.sort(lambda x, y: cmp(x.score.index, y.score.index))
   governors = tuple(governors)

   components = [ ] 
   for governor in governors:
      for component in naive_forward_in_expr(governor, _Component):
         if component.offset.prolated.start <= prolated_offset:
            if prolated_offset < component.offset.prolated.stop:
               components.append(component)
   components.sort(lambda x, y: cmp(x.score.index, y.score.index))
   components = tuple(components)

   vertical_moment = VerticalMoment(prolated_offset, governors, components)

   return vertical_moment
