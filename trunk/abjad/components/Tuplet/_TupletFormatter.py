from abjad.components.Container._ContainerFormatter import _ContainerFormatter
from abjad.components.Tuplet._TupletFormatterSlotsInterface import _TupletFormatterSlotsInterface


class _TupletFormatter(_ContainerFormatter):

   def __init__(self, client):
      _ContainerFormatter.__init__(self, client)
      self.label = None
      self._slots = _TupletFormatterSlotsInterface(self)

   ## PRIVATE ATTRIBUTES ##

   @property
   def _fraction(self):
      tuplet = self._client
      if tuplet._visible:
         if tuplet.duration.augmentation or \
            tuplet.duration._is_nonbinary or \
            tuplet.force_fraction:
               return r'\fraction '
      return ''

   ## PUBLIC ATTRIBUTES ##

   @property
   def slots(self):
      return self._slots

   @property
   def tuplet(self):
      return self._client
