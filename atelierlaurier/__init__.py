# -*- coding: utf-8 -*-

from pkg_resources import get_distribution

from pyramid.config import Configurator

from git import Repo

from atelierlaurier.lib.request import AtelierLaurierRequest


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    repo_path = get_distribution("atelierlaurier").location

    settings["config_uri"] = global_config["__file__"]
    settings["asset_version"] = Repo(repo_path).head.commit.hexsha

    settings.setdefault("jinja2.i18n.domain", "atelierlaurier")

    config = Configurator(settings=settings,
                          request_factory=AtelierLaurierRequest)

    config.include("atelierlaurier.jinja")
    config.include("atelierlaurier.route")
    config.include("atelierlaurier.renderers")

    static_url = config.registry.settings.get("app.static.url", "static")
    config.registry.settings["app.static.url"] = static_url
    config.add_static_view(static_url, "%s:static" % __name__.split(".")[0],
                           cache_max_age=3600)

    config.scan("atelierlaurier.subscribers")
    config.scan("atelierlaurier.views")

    return config.make_wsgi_app()
