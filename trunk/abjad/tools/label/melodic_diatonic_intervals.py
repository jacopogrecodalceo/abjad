from abjad.leaf import _Leaf
from abjad.note import Note
from abjad.tools import iterate


def melodic_diatonic_intervals(expr):
   r""".. versionadded:: 1.1.2

   Label the melodic diatonic interval of every leaf in `expr`. ::

      abjad> staff = Staff(construct.notes([0, 25, 11, -4, -14, -13, 9, 10, 6, 5], [Rational(1, 8)]))
      abjad> label.melodic_diatonic_intervals(staff)
      abjad> f(staff)
      \new Staff {
              c'8 ^ \markup { +aug15 }
              cs'''8 ^ \markup { -M9 }
              b'8 ^ \markup { -aug9 }
              af8 ^ \markup { -m7 }
              bf,8 ^ \markup { +aug1 }
              b,8 ^ \markup { +m14 }
              a'8 ^ \markup { +m2 }
              bf'8 ^ \markup { -dim4 }
              fs'8 ^ \markup { -aug1 }
              f'8
      }
   """
   from abjad.tools import pitchtools

   for note in iterate.naive_forward_in(expr, Note):
      thread_iterator = iterate.thread_forward_from(note, _Leaf)
      try:
         thread_iterator.next( )
         next_leaf = thread_iterator.next( )
         if isinstance(next_leaf, Note):
            mdi = pitchtools.melodic_diatonic_interval_from_to(note, next_leaf)
            note.markup.up.append(mdi)
      except StopIteration:
         pass
