#!/usr/bin/env python2.7

import visualpipes.block
import visualpipes.formats

class Create(visualpipes.block.Block):
    def __init__(self, data=False):
        super(Create, self).__init__(
            name = 'Read file',
            connectors_input = [
                [visualpipes.formats.STRING, False],
            ],
            connectors_output = [
                [visualpipes.formats.ANY],
            ],
            connectors_output_failed = [ 
                [visualpipes.formats.STRING],
            ]
        )
