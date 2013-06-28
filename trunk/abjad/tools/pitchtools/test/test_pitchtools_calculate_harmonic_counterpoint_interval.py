from abjad import *


def test_pitchtools_calculate_harmonic_counterpoint_interval_01():
    '''Ascending intervals greater than an octave.
    '''

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(-3), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(10)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(-2), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(9)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(-1), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(9)


def test_pitchtools_calculate_harmonic_counterpoint_interval_02():
    '''Ascending octave.
    '''

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(0), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(8)


def test_pitchtools_calculate_harmonic_counterpoint_interval_03():
    '''Ascending intervals less than an octave.
    '''

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(9), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(3)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(10), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(2)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(11), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(2)


def test_pitchtools_calculate_harmonic_counterpoint_interval_04():
    '''Unison.
    '''

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(12))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(1)


def test_pitchtools_calculate_harmonic_counterpoint_interval_05():
    '''Descending intervals greater than an octave.
    '''

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(-3))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(10)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(-2))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(9)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(-1))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(9)


def test_pitchtools_calculate_harmonic_counterpoint_interval_06():
    '''Descending octave.
    '''

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(0))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(8)


def test_pitchtools_calculate_harmonic_counterpoint_interval_07():
    '''Descending intervals less than an octave.
    '''

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(9))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(3)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(10))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(2)

    hcpi = pitchtools.calculate_harmonic_counterpoint_interval(
        pitchtools.NamedChromaticPitch(12), pitchtools.NamedChromaticPitch(11))
    assert hcpi == pitchtools.HarmonicCounterpointInterval(2)
