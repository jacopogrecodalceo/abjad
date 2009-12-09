from abjad.tools.pitchtools.melodic_diatonic_interval_from_to import \
   melodic_diatonic_interval_from_to


def harmonic_chromatic_interval_class_from_to(pitch_carrier_1, pitch_carrier_2):
   '''.. versionadded:: 1.1.2

   Return harmonic chromatic interval class from `pitch_carrier_1` to
   `pitch_carrier_2`. ::

      abjad> pitchtools.harmonic_chromatic_interval_class_from_to(Pitch(-2), Pitch(12))
      HarmonicChromaticIntervalClass(2)

   ::

      abjad> pitchtools.harmonic_chromatic_interval_class_from_to(Pitch(12), Pitch(-2))
      HarmonicChromaticIntervalClass(2)
   '''

   ## get melodic diatonic interval
   mdi = melodic_diatonic_interval_from_to(pitch_carrier_1, pitch_carrier_2)

   ## return harmonic chromatic interval class
   return mdi.harmonic_chromatic_interval.interval_class
