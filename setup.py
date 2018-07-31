import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

setup(
    name="atelierlaurier",
    version="1.0.0",
    description="L'atelier Laurier",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="web wsgi bfg pylons pyramid",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="atelierlaurier",
    install_requires=[
        "alembic",
        "ansible",
        "Babel",
        "bumpversion",
        "circus",
        "chaussette",
        "decorator",
        "docopt",
        "dogpile.cache",
        "GitPython",
        "jinja2",
        "markdown2",
        "pyramid>=1.5",
        "pyramid_jinja2>=2.0",
        "pyramid_beaker",
        "pyramid_debugtoolbar",
        "pyramid_tm",
        "pyScss",
        "raven",
        "transaction",
        "unicodecsv",
        "waitress",
        "webhelpers",
        "zope.sqlalchemy",
    ],
    extras_require={
        'dev': {
            "pip-tools",
        },
    },
    entry_points="""\
        [paste.app_factory]
        main = atelierlaurier:main
    """,
    message_extractors={".": [
        ("**.py", "lingua_python", None),
        ("**.jinja2", "jinja2", None)
    ]},
)
