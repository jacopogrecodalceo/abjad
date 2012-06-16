from experimental.specificationtools.exceptions import *
from abjad.tools.abctools.AbjadObject import AbjadObject
from collections import OrderedDict


class ContextProxy(AbjadObject, OrderedDict):

    ### INITIALIZER ###

    def __init__(self):
        OrderedDict.__init__(self)

    ### SPECIAL METHODS ###

    def __repr__(self):
        return OrderedDict.__repr__(self)

    ### READ-ONLY PRIVATE PROPERTIES ###

    @property
    def _mandatory_argument_values(self):
        return self.items()

    ### PUBLIC METHODS ###

    def get_setting(self, attribute=None, timespan=None):
        settings = self.get_settings(attribute=attribute, timespan=timespan)
        if not settings:
            raise MissingSettingError('no settings for {!r} found.'.format(attribute))
        elif 1 < len(settings):
            raise ExtraSettingError('multiple settings for {!r} found.'.format(attribute))
        assert len(settings) == 1
        return settings[0]

    def get_settings(self, attribute=None, timespan=None):
        settings = []
        for key, setting in self.iteritems():
            if ((attribute is None or key == attribute) and
                (timespan is None or setting.timespan == timespan)
                ):
                settings.append(setting)
        return settings
