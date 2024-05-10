# A function for getting the current version of the library

class VersionUtil:
    @staticmethod
    def get_version():
        """
        Retrieves the current version of the library from a VERSION file or other source.

        Returns:
            str: A string representing the version.
        """
        try:
            with open("VERSION", "r") as version_file:
                return version_file.read().strip()
        except FileNotFoundError:
            return "unknown"  # Fallback version if the VERSION file is not found
