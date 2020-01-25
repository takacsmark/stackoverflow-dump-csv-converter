import unittest

from utils import *

class TestArguments(unittest.TestCase):

    valid_workdir = "/Volumes/Samsung_T5/data/SO_archive_2019_12/"
    
    def test_f_only(self):
        args = [
           "-f",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, True)
        self.assertEqual(progress_bar, False)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_force_only(self):
        args = [
           "--force",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, True)
        self.assertEqual(progress_bar, False)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_p_only(self):
        args = [
           "-p",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, False)
        self.assertEqual(progress_bar, True)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_progress_bar_only(self):
        args = [
           "--progress-bar",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, False)
        self.assertEqual(progress_bar, True)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_f_and_p(self):
        args = [
           "-f",
           "-p",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, True)
        self.assertEqual(progress_bar, True)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_force_and_progress_bar(self):
        args = [
           "--force",
           "--progress-bar",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, True)
        self.assertEqual(progress_bar, True)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_options_reverse_order(self):
        args = [
           "--progress-bar",
           "--force",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, True)
        self.assertEqual(progress_bar, True)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_f_and_force(self):
        args = [
           "-f",
           "--force",
           "Tags",
           self.valid_workdir,
        ]

        force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(force_overwrite, True)
        self.assertEqual(progress_bar, False)
        self.assertEqual(filename, "Tags")
        self.assertEqual(workdir, self.valid_workdir)
        self.assertEqual(release, None)

    def test_invalid_option(self):
        args = [
           "-f",
           "-a",
           "Tags",
           self.valid_workdir,
        ]

        with self.assertRaises(SystemExit) as cm:
            force_overwrite, progress_bar, filename, workdir, release = init_from_arguments(args)
        
        self.assertEqual(cm.exception.code, 1)

if __name__ == "__main__":
    unittest.main()
