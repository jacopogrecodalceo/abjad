import abc
#from experimental.tools.settingtools.Expression import Expression
from abjad.tools.abctools.AbjadObject import AbjadObject


#class LookupMethodMixin(Expression):
class LookupMethodMixin(AbjadObject):
    '''Lookup method mixin.

    ::

        >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
        >>> score_specification = specificationtools.ScoreSpecification(score_template=score_template)
        >>> red_segment = score_specification.append_segment(name='red')

    Base class.
    '''
    
#    ### CLASS ATTRIBUTES ###
#
#    __metaclass__ = abc.ABCMeta
#
#    ### INITIALIZER ###
#
#    @abc.abstractmethod
#    def __init__(self, anchor=None):
#        Expression.__init__(self, anchor=anchor)

    ### PUBLIC METHODS ###

    def look_up_division_setting(self, voice):
        r'''Look up voice ``1`` division command
        active at start of segment ``'red'``::

            >>> request = red_segment.timespan.start_offset.look_up_division_setting('Voice 1')

        ::

            >>> z(request)
            requesttools.DivisionSettingLookupRequest(
                voice_name='Voice 1',
                offset=settingtools.OffsetExpression(
                    anchor=settingtools.TimespanExpression(
                        anchor='red'
                        )
                    )
                )

        Return command request.        
        '''
        from experimental.tools import requesttools
        return requesttools.DivisionSettingLookupRequest(voice, offset=self)

    def look_up_rhythm_setting(self, voice):
        r'''PayloadCallbackMixin voice ``1`` rhythm command 
        active at start of segment ``'red'``::

            >>> request = red_segment.timespan.start_offset.look_up_rhythm_setting('Voice 1')

        ::

            >>> z(request)
            requesttools.RhythmSettingLookupRequest(
                voice_name='Voice 1',
                offset=settingtools.OffsetExpression(
                    anchor=settingtools.TimespanExpression(
                        anchor='red'
                        )
                    )
                )

        Return command request.        
        '''
        from experimental.tools import requesttools
        return requesttools.RhythmSettingLookupRequest(voice, offset=self)

    def look_up_time_signature_setting(self, voice):
        r'''PayloadCallbackMixin voice ``1`` time signature command
        active at start of segment ``'red'``::

            >>> request = red_segment.timespan.start_offset.look_up_time_signature_setting('Voice 1')

        ::

            >>> z(request)
            requesttools.TimeSignatureSettingLookupRequest(
                voice_name='Voice 1',
                offset=settingtools.OffsetExpression(
                    anchor=settingtools.TimespanExpression(
                        anchor='red'
                        )
                    )
                )

        Return command request.
        '''
        from experimental.tools import requesttools
        return requesttools.TimeSignatureSettingLookupRequest(voice, offset=self)
