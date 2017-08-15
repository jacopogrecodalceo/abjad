def timespan_2_starts_when_timespan_1_starts(
    timespan_1=None,
    timespan_2=None,
    hold=False,
    ):
    r'''Makes time relation indicating that `timespan_2` starts
    when `timespan_1` starts.

    ..  container:: example

        ::

            >>> relation = abjad.timespantools.timespan_2_starts_when_timespan_1_starts()
            >>> f(relation)
            abjad.timespantools.TimespanTimespanTimeRelation(
                inequality=abjad.timespantools.CompoundInequality(
                    [
                        abjad.TimespanInequality('timespan_1.start_offset == timespan_2.start_offset'),
                        ],
                    logical_operator='and',
                    ),
                )

    Returns time relation or boolean.
    '''
    from abjad.tools import timespantools

    inequality = timespantools.CompoundInequality([
        'timespan_1.start_offset == timespan_2.start_offset',
        ])

    time_relation = timespantools.TimespanTimespanTimeRelation(
        inequality,
        timespan_1=timespan_1,
        timespan_2=timespan_2,
        )

    if time_relation.is_fully_loaded and not hold:
        return time_relation()
    else:
        return time_relation
