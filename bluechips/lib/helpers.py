"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to both as 'h'.
"""
from routes import url_for, redirect_to
from webhelpers.html import escape, literal, url_escape
from webhelpers.html.tags import *

def bluechips():
    return '<span class="bluechips">BlueChips</span>'
