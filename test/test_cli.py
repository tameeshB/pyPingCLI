"""Tests for main cli landing scripts."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from pypingcli import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['pyping', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['pyping', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['pyping', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)