#!/usr/bin/env python
import gcn
from morgoth.handler import handler
from morgoth import morgoth_config

testing = True
if not testing:
    gcn.listen(handler=handler, port=morgoth_config["pygcn"]["port"])
else:
    from lxml.etree import fromstring
    import pkg_resources
    payload = pkg_resources.resource_string(__name__, '../morgoth/data/gbm_flt.xml')
    handler(payload, fromstring(payload))
