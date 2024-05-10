"""Unit tests for the VersionUtil class in the lib_version_group3 package."""

import unittest
from lib_version_group3.version import VersionUtil, __version__


class TestVersionUtil(unittest.TestCase):
    """Tests for verifying the functionality of the VersionUtil class."""

    def test_get_version(self):
        """Test that the get_version method returns the correct version."""
        expected_version = __version__
        received_version = VersionUtil.get_version()

        self.assertEqual(received_version, expected_version,
                         "The version returned by VersionUtil.get_version() "
                         "should match the __version__ constant.")


if __name__ == '__main__':
    unittest.main()
