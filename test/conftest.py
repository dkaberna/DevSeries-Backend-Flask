"""Shared fixtures."""

import pytest

from models.employee import *
my_employee = employee()

@pytest.fixture
def employee():
    """Returns employee object"""
    try:
        return my_employee
    except:
        print ("Unable to read database")