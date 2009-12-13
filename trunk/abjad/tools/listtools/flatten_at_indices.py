from abjad.tools.listtools.flatten import flatten


def flatten_at_indices(l, indices, ltypes = (list, tuple), depth = -1):
   '''.. versionadded:: 1.1.2

   Flatten nested lists at `indices` in `l`.  ::

      abjad> l = [0, 1, [2, 3, 4], [5, 6, 7]]
      abjad> listtools.flatten_at_indices(l, [3])
      [0, 1, [2, 3, 4], 5, 6, 7]

   Negative indices are supported. ::

      abjad> l = [0, 1, [2, 3, 4], [5, 6, 7]]
      abjad> listtools.flatten_at_indices(l, [-1])
      [0, 1, [2, 3, 4], 5, 6, 7]
   '''

   if not isinstance(l, ltypes):
      raise TypeError( )
   ltype = type(l)

   len_l = len(l)
   indices = [x if 0 <= x else len_l + x for x in indices]

   result = [ ]
   for i, element in enumerate(l):
      if i in indices:
         try:
            flattened = flatten(element, ltypes = ltypes, depth = depth)
            result.extend(flattened)
         except:
            result.append(element)
      else:
         result.append(element)

   result = ltype(result)
   return result
