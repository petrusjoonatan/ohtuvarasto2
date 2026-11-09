from urllib import request

import tomli
from packaging.requirements import Requirement

from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        
        with request.urlopen(self._url) as response:
            content = response.read().decode("utf-8")

        data = tomli.loads(content)
        project = data["project"]
        dependencies = [
            Requirement(dependency).name
            for dependency in project.get("dependencies", [])
        ]
        if project.get("requires-python"):
            dependencies.insert(0, "python")

        dev_dependencies = [
            Requirement(dependency).name
            for dependency in data.get("dependency-groups", {}).get("dev", [])
        ]
        authors = [author["name"] for author in project.get("authors", [])]

        return Project(
            name=project["name"],
            description=project.get("description", ""),
            dependencies=dependencies,
            dev_dependencies=dev_dependencies,
            license=project.get("license", ""),
            authors=authors,
        )
