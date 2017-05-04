# -*- coding: utf-8 -*-
from abjad.tools.abctools import AbjadValueObject


class BowPressure(AbjadValueObject):
    r'''Bow pressure indicator.

    ..  container:: example

        Overpressure indicator:

        ..  container:: example

            ::

                >>> bow_pressure = indicatortools.BowPressure('overpressure')
                >>> print(format(bow_pressure))
                indicatortools.BowPressure(
                    pressure='overpressure',
                    )

    ..  container:: example

        Underpressure indicator:

        ..  container:: example

            ::

                >>> bow_pressure = indicatortools.BowPressure('underpressure')
                >>> print(format(bow_pressure))
                indicatortools.BowPressure(
                    pressure='underpressure',
                    )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_default_scope',
        '_pressure',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pressure=None,
        ):
        self._default_scope = None
        self._pressure = pressure

    ### PUBLIC PROPERTIES ###

    @property
    def default_scope(self):
        r'''Gets default scope of bow pressure indicator.

        ..  container:: example

            ::

                >>> bow_pressure = indicatortools.BowPressure('overpressure')
                >>> bow_pressure.default_scope is None
                True

        Returns none.
        '''
        return self._default_scope

    @property
    def pressure(self):
        r'''Gets pressure of indicator.

        ..  container:: example

            Overpressure:

            ::

                >>> bow_pressure = indicatortools.BowPressure('overpressure')
                >>> bow_pressure.pressure
                'overpressure'

        ..  container:: example

            Underpressure:

            ::

                >>> bow_pressure = indicatortools.BowPressure('underpressure')
                >>> bow_pressure.pressure
                'underpressure'

        Returns string.
        '''
        return self._pressure
