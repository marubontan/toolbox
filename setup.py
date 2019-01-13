from distutils.core import setup


def parse_requirements(fname):
    dependencies = open(fname).read().split("\n")
    for dependency in dependencies:
        clean_dependency = dependency.strip(' ')
        if clean_dependency:
            yield clean_dependency


setup(name="toolbox",
      version="1.0.0",
      install_requires=list(parse_requirements('requirements.txt')), )
