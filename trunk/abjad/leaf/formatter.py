from abjad.core.formatter import _Formatter
from abjad.core.formatcarrier import _FormatCarrier
from abjad.leaf.number import _LeafFormatterNumberInterface


class _LeafFormatter(_Formatter):

   def __init__(self, client):
      _Formatter.__init__(self, client)
      self._number = _LeafFormatterNumberInterface(self)

   ## PUBLIC ATTRIBUTES ##

   @property
   def agrace(self):
      result = [ ]
      agrace = self._client.grace.after
      if len(agrace) > 0:
         result.append(agrace.format)
      return result

   @property
   def agrace_opening(self):
      if len(self._client.grace.after) > 0:
         return [r'\afterGrace']
      else:
         return [ ] 

   @property
   def body(self):
      client = self._client
      annotations = client.annotations
      interfaces = client.interfaces
      spanners = client.spanners
      result = [ ]

      result.extend(annotations.left)
      result.extend(spanners.left)
      result.extend(interfaces.left)
      #result.extend(client.body)
      result.extend(self.nucleus)
      result.extend(self.tremolo)
      result.extend(interfaces.right)
      result.extend(spanners.right)
      result.extend(annotations.right)
      result.extend(self.number_contribution)
      result.extend(self.comments_right)
      return [' '.join(result)]

   @property
   def clef(self):
      result = [ ]
      if hasattr(self._client, '_clef'):
         result.append(self._client._clef.format)
      return result

   @property
   def comments_right(self):
      result = [ ]
      result.extend(['% ' + x for x in self._client.comments.right])
      return result

   @property
   def format(self):
      client = self._client
      annotations = client.annotations
      interfaces = client.interfaces
      spanners = client.spanners
      result = [ ]
      result.extend(self.comments_before)
      result.extend(annotations.before) 
      result.extend(self.grace)
      result.extend(interfaces.overrides)
      result.extend(spanners.before)
      result.extend(interfaces.before)
      result.extend(interfaces.opening)
      result.extend(self.agrace_opening)
      result.extend(self.body)
      result.extend(self.agrace)
      result.extend(interfaces.closing)
      result.extend(interfaces.after)
      result.extend(spanners.after)
      result.extend(annotations.after)
      result.extend(self.comments_after)
      return '\n'.join(result)

   @property
   def grace(self):
      result = [ ]
      grace = self._client.grace.before
      if len(grace) > 0:
         result.append(grace.format)
      return result

   @property
   def nucleus(self):
      return self._client.body

   @property
   def number(self):
      return self._number

   @property
   def number_contribution(self):
      result = [ ]
      client = self._client
      contribution = self.number._leaf_contribution
      if contribution == 'markup':
         result.append(r'^ \markup { %s }' % client.numbering.leaf)
      elif contribution == 'comment':
         result.append(r'%% leaf %s' % client.numbering.leaf)
      return result

   @property
   def tremolo(self):
      result = [ ]
      subdivision = self._client.tremolo.subdivision
      if subdivision:
         result.append(':%s' % subdivision) 
      return result
