from abjad import *


def test_container_ids_01( ):
   '''
   Container music lists are unique per instance,
   rather than shared between different instances.
   '''

   t1 = Container( )
   t2 = Container( )

   assert id(t1._music) != id(t2._music)
