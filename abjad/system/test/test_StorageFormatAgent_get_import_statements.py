import abjad


def test_StorageFormatAgent_get_import_statements_01():
    subject = abjad.NamedPitch()
    agent = abjad.StorageFormatManager(subject)
    assert agent.get_import_statements() == (
        'from abjad import pitch',
        )


def test_StorageFormatAgent_get_import_statements_02():
    subject = abjad.Selection()
    agent = abjad.StorageFormatManager(subject)
    assert agent.get_import_statements() == (
        'from abjad import core',
        )


def test_StorageFormatAgent_get_import_statements_03():
    subject = [
        abjad.TimeSignature((3, 4)),
        abjad.TimeSignature((4, 4)),
        ]
    agent = abjad.StorageFormatManager(subject)
    assert agent.get_import_statements() == (
        'from abjad import indicators',
        )
