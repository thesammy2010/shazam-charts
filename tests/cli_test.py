import sys
import logging
from unittest import TestCase, mock
from argparse import Namespace

from shazam_charts.run import main, parse_args, are_args_valid


class CLIArgsTest(TestCase):
    """
    This class contains all the tests for the CLI part of this code
    """

    def setUp(self) -> None:
        logging.basicConfig(level=logging.CRITICAL)

    def tearDown(self) -> None:
        logging.basicConfig(level=logging.WARNING)

    def test_valid_no_verbose(self) -> None:
        """
        Tests if the verbose option is set to false when not supplied
        :return: Nothing
        """
        self.assertTupleEqual(parse_args(["chart", "1"]), (Namespace(verbose=False, method="chart", count=1), []))

    def test_valid_with_verbose(self) -> None:
        """
        Tests if the verbose option is set to true when supplied with -v or --verbose
        :return: Nothing
        """
        self.assertTupleEqual(parse_args(["chart", "1", "-v"]), (Namespace(verbose=True, method="chart", count=1), []))
        self.assertTupleEqual(
            parse_args(["chart", "1", "--verbose"]), (Namespace(verbose=True, method="chart", count=1), [])
        )

    def test_args_valid(self) -> None:
        """
        Tests if the validate_args method works when valid arguments are supplied
        :return: Nothing
        """
        self.assertTrue(are_args_valid(args=Namespace(verbose=True, method="chart", count=1), unknown=[]))
        self.assertTrue(are_args_valid(args=Namespace(verbose=False, method="chart", count=1), unknown=[]))
        self.assertTrue(are_args_valid(args=Namespace(verbose=False, method="chart", count=10), unknown=[]))
        self.assertTrue(are_args_valid(args=Namespace(verbose=True, method="state_chart", count=1), unknown=[]))
        self.assertTrue(are_args_valid(args=Namespace(verbose=False, method="state_chart", count=1), unknown=[]))
        self.assertTrue(are_args_valid(args=Namespace(verbose=False, method="state_chart", count=10), unknown=[]))

    def test_args_invalid(self) -> None:
        """
        Tests if the validate_args method works when invalid arguments are supplied
        :return: Nothing
        """
        self.assertFalse(are_args_valid(args=Namespace(verbose=False, method="chart", count=0), unknown=[]))
        self.assertFalse(are_args_valid(args=Namespace(verbose=False, method="chart", count=-1), unknown=[]))
        self.assertFalse(are_args_valid(args=Namespace(verbose=False, method="chart", count=1), unknown=["-x y"]))
        self.assertFalse(are_args_valid(args=Namespace(verbose=False, method="state", count=-1), unknown=[]))

    @mock.patch.object(sys, "argv", ["shazam-charts", "chart", "1"])
    @mock.patch.object(sys, "exit", lambda x: None)
    @mock.patch("shazam_charts.run.transform")
    def test_e2e_run_1(self, mocked_method: mock.MagicMock) -> None:
        """
        Tests a end to end test to see if passing the CLI arguments as shown gives the intended output
        :param mocked_method: A MagicMock, we don't want to call the run method
        :return: Nothing
        """
        main()
        mocked_method.assert_called_once_with(method="chart", count=1)

    @mock.patch.object(sys, "argv", ["shazam-charts", "state_chart", "1"])
    @mock.patch.object(sys, "exit", lambda x: None)
    @mock.patch("shazam_charts.run.transform")
    def test_e2e_run_2(self, mocked_method: mock.MagicMock) -> None:
        """
        Tests a end to end test to see if passing the CLI arguments as shown gives the intended output
        :param mocked_method: A MagicMock, we don't want to call the run method
        :return: Nothing
        """
        main()
        mocked_method.assert_called_once_with(method="state_chart", count=1)
