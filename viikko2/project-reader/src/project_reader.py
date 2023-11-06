from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        body = parsed_toml['tool']['poetry']
        name = body['name']
        description = body['description']
        dependencies = body['dependencies']
        dev_dependencies = body['group']['dev']['dependencies']
        authors = body['authors']
        license = body['license']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, authors, license)
