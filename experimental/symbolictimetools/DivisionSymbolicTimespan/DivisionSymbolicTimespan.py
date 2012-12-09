from abjad.tools import durationtools
from experimental import divisiontools
from abjad.tools import timerelationtools
from experimental.symbolictimetools.TimeRelationSymbolicTimespan import TimeRelationSymbolicTimespan


class DivisionSymbolicTimespan(TimeRelationSymbolicTimespan):
    r'''.. versionadded:: 1.0

    ::

        >>> from experimental import *

    Select all divisions that start during score::

        >>> symbolictimetools.DivisionSymbolicTimespan()
        DivisionSymbolicTimespan()

    Select all divisions that start during segment ``'red'``::

        >>> division_selector = symbolictimetools.DivisionSymbolicTimespan(anchor='red')

    ::

        >>> z(division_selector)
        symbolictimetools.DivisionSymbolicTimespan(
            anchor='red'
            )

    Select the last two divisions that start during segment ``'red'``::

        >>> division_selector = symbolictimetools.DivisionSymbolicTimespan(anchor='red', start_identifier=-2)

    ::

        >>> z(division_selector)
        symbolictimetools.DivisionSymbolicTimespan(
            anchor='red',
            start_identifier=-2
            )

    Division selectors are immutable.
    '''

    ### PUBLIC METHODS ###

    def get_offsets(self, score_specification, voice_name, start_segment_name=None):
        '''Evaluate start and stop offsets of selecto when applied
        to `voice_name` in `score_specification`.

        .. note:: add example.

        Return pair.
        '''
        divisions = self.get_selected_objects(score_specification, voice_name)
        start_offset = divisions[0].start_offset
        stop_offset = divisions[-1].stop_offset
        return start_offset, stop_offset
        
    # TODO: eventually return selection
    def get_selected_objects(self, score_specification, voice_name):
        '''Get divisions selected when selector is applied
        to `voice_name` in `score_specification`.

        .. note:: add example.
        
        Return list of zero or more offset-positioned divisions.
        '''
        voice_division_list = score_specification.contexts[voice_name]['voice_division_list']
        divisions = []
        segment_specification = score_specification.get_start_segment_specification(self.anchor)
        timespan_1 = segment_specification.timespan
        if self.time_relation is None:
            time_relation = timerelationtools.timespan_2_starts_during_timespan_1(timespan_1=timespan_1)
        else:
            time_relation = self.time_relation
            time_relation._timespan_1 = timespan_1
        for division in voice_division_list:
            if time_relation(timespan_2=division, 
                score_specification=score_specification, 
                context_name=voice_name):
                divisions.append(division)
        divisions = divisions[self.start_identifier:self.stop_identifier]
        #self._debug(divisions, 'divisions')
        return divisions
    
    def set_segment_identifier(self, segment_identifier):
        '''Delegate to ``self.time_relation.set_segment_identifier()``.
        '''
        self.time_relation.set_segment_identifier(segment_identifier)
