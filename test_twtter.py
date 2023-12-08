import pytest
from twttr import shorten

def test_non_str():
    assert shorten("750") == "750"

def test_caps():
    assert shorten("ALIBABA") == "LBB"

def test_lower():
    assert shorten("grapefruit") == "grpfrt"

def test_0_vowels():
    assert shorten("dry") == "dry"

def test_punct():
    assert shorten("AI.") == "."
