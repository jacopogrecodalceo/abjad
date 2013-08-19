# -*- encoding: utf-8 -*-


def calculate_harmonic_counterpoint_interval_class(pitch_carrier_1, pitch_carrier_2):
    '''Calculate harmonic counterpoint interval-class from `pitch_carrier_1` to
    `pitch_carrier_2`:

    ::

        >>> pitchtools.calculate_harmonic_counterpoint_interval_class(
        ... pitchtools.NamedChromaticPitch(-2), pitchtools.NamedChromaticPitch(12))
        HarmonicCounterpointIntervalClass(2)

    Return harmonic counterpoint interval-class.
    '''
    from abjad.tools import pitchtools

    # get melodic diatonic interval
    mdi = pitchtools.MelodicDiatonicInterval.from_pitch_carriers(
        pitch_carrier_1, pitch_carrier_2)

    # return harmonic counterpoint interval-class
    return mdi.harmonic_counterpoint_interval.harmonic_counterpoint_interval_class
