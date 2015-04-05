# -*- coding: utf-8 -*-

import logging

from functools import partial
from os.path import dirname, join

from pyramid.events import (ApplicationCreated, BeforeRender, NewRequest,
                            subscriber)
from pyramid.asset import abspath_from_asset_spec
from pyramid.settings import asbool

from atelierlaurier.lib.jinja2 import add_renderer_globals
from atelierlaurier.lib import scss

log = logging.getLogger(__name__)


@subscriber(ApplicationCreated)
def _initialize(event):
    settings = event.app.registry.settings
    if not asbool(settings.get('scss.reload')):
        log.debug('On-the-fly SCSS compilation disabled')
        compile.closure = lambda: None
        return
    log.debug('On-the-fly SCSS compilation launched')
    app_name = __name__.split('.')[0]
    scss.initialize(
        settings['app.static.url'],
        abspath_from_asset_spec(':'.join([app_name, 'static'])))
    assets_dir = abspath_from_asset_spec(settings['scss.directory'])
    bootstrap_dir = join(dirname(dirname(__file__)),
                         'libs', 'bootstrap-sass', 'vendor', 'assets',
                         'stylesheets')
    options = dict(load_paths=[assets_dir, bootstrap_dir],
                   compress=asbool(settings.get('scss.compress')))
    compile.closure = partial(scss.compile, assets_dir, options)


@subscriber(NewRequest)
def compile(event):
    compile.closure()


@subscriber(BeforeRender)
def _add_renderer_globals(event):
    app_name = __name__.split('.')[0]
    add_renderer_globals(app_name, event)
