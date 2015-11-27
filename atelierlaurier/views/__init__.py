# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import atelierlaurier

from pyramid.response import FileResponse
from pyramid.view import view_config

from atelierlaurier.lib.collection import triplets


@view_config(route_name="favicon")
def favicon_view(request):
    root = os.path.dirname(atelierlaurier.__file__)
    static = request.registry.settings["app.static.url"]
    icon = os.path.join(root, static, "favicon.ico")
    return FileResponse(icon, request=request)


@view_config(route_name="index", renderer="index.jinja2")
def index(request, **kwargs):
    return dict(triplets=triplets(36))
