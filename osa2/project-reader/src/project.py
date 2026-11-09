class Project:
    def __init__(
        self, name, description, dependencies, dev_dependencies,
        license="", authors=None,
    ):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors if authors is not None else []

    def _stringify_list(self, items):
        return "\n".join(f"- {item}" for item in items) if items else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{self._stringify_list(self.authors)}"
            f"\n\nDependencies:\n{self._stringify_list(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n"
            f"{self._stringify_list(self.dev_dependencies)}"
        )
