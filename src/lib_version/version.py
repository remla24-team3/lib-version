"""This file contains the version of the library."""
# pylint: disable=all


class VersionUtil:
    @staticmethod
    def get_version():
        try:
            with open("version.py", "r") as file:
                version_line = file.readline()
                version = version_line.split("'")[1]
                return version
        except FileNotFoundError:
            return "Version file not found."


# Usage
version_util = VersionUtil()
print("Library Version:", version_util.get_version())
