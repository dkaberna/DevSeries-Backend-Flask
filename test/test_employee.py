"""
test_app.py
--------
Provides unit test functionality via PyTest framework

"""

import pytest

#Verifies employee details match database
def test_lookup_by_name(employee):
    name = employee[0]["name"]
    title = employee[0]["title"]
    assert "Cranston, Bryan" == name
    assert "Mission Lead" == title