# -*- coding: utf-8 -*-
from abjad.tools.abctools.AbjadValueObject import AbjadValueObject


class BendAfter(AbjadValueObject):
    r'''Fall or doit.

    ::

        >>> import abjad

    ..  container:: example

        A fall:

        ::

            >>> note = abjad.Note("c'4")
            >>> bend = abjad.BendAfter(-4)
            >>> abjad.attach(bend, note)
            >>> show(note) # doctest: +SKIP

        ..  docs::

            >>> f(note)
            c'4 - \bendAfter #'-4.0

    ..  container:: example

        A doit:

        ::

            >>> note = abjad.Note("c'4")
            >>> bend = abjad.BendAfter(2)
            >>> abjad.attach(bend, note)
            >>> show(note) # doctest: +SKIP

        ..  docs::

            >>> f(note)
            c'4 - \bendAfter #'2.0

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_bend_amount',
        '_default_scope',
        )

    _format_slot = 'right'

    _split_direction = Right

    ### INITIALIZER ###

    def __init__(self, bend_amount=-4):
        if isinstance(bend_amount, type(self)):
            bend_amount = bend_amount.bend_amount
        bend_amount = float(bend_amount)
        self._bend_amount = bend_amount
        self._default_scope = None

    ### SPECIAL METHODS ###

    def __str__(self):
        r'''Gets string representation of bend after.

        ..  container:: example

            ::

                >>> str(abjad.BendAfter())
                "- \\bendAfter #'-4.0"

        Returns string.
        '''
        return r"- \bendAfter #'{}".format(self.bend_amount)

    ### PRIVATE PROPERTIES ###

    @property
    def _contents_repr_string(self):
        return str(self.bend_amount)

    ### PRIVATE METHODS ###

    def _get_lilypond_format(self):
        return str(self)

    def _get_lilypond_format_bundle(self, component=None):
        from abjad.tools import systemtools
        lilypond_format_bundle = systemtools.LilyPondFormatBundle()
        lilypond_format_bundle.right.articulations.append(str(self))
        return lilypond_format_bundle

    ### PUBLIC PROPERTIES ###

    @property
    def bend_amount(self):
        r'''Gets bend amount of bend after.

        ..  container:: example

            Fall:

            ::

                >>> bend = abjad.BendAfter(-4)
                >>> bend.bend_amount
                -4.0

        ..  container:: example

            Doit:

            ::

                >>> bend = abjad.BendAfter(2)
                >>> bend.bend_amount
                2.0 

        Returns float.
        '''
        return self._bend_amount

    @property
    def default_scope(self):
        r'''Gets default scope of bend after.

        ..  container:: example

            >>> bend = abjad.BendAfter(-4)
            >>> bend.default_scope is None
            True

        Returns none.
        '''
        return self._default_scope
