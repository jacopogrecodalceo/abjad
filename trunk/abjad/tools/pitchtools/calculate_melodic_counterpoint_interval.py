# -*- encoding: utf-8 -*-


def calculate_melodic_counterpoint_interval(pitch_carrier_1, pitch_carrier_2):
    '''Calculate melodic counterpoint interval `pitch_carrier_1` to
    `pitch_carrier_2`:

    ::

        >>> pitchtools.calculate_melodic_counterpoint_interval(
        ... pitchtools.NamedChromaticPitch(-2), pitchtools.NamedChromaticPitch(12))
        MelodicCounterpointInterval(+9)

    Return melodic counterpoint interval.
    '''
    from abjad.tools import pitchtools

    # get melodic diatonic interval
    mdi = pitchtools.MelodicDiatonicInterval.from_pitch_carriers(pitch_carrier_1, pitch_carrier_2)

    # return melodic counterpoint interval
    return mdi.melodic_counterpoint_interval
