# -*- coding: utf-8 -*-
# __file__  : test_tmpdir.py
# __time__  : 2020/7/3 5:43 PM

# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0

from pytest import ExitCode
import pytest
# @pytest.mark.slow

