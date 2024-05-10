# A class for getting the current version of the library

import pkg_resources


class VersionUtil:
    @staticmethod
    def get_version():
        try:
            # Takes the package name as input
            return pkg_resources.get_distribution('src').version 
        except pkg_resources.DistributionNotFound:
            return "Unknown version"
