import pytest
from main import *

def test_msgValueExtractor():
    x = msgValueExtractor()
    assert type(x) == str
    assert (re.findall('(?<=msg=)(.*)(?=\W\n)',x)) == x

def test_logFile():
    x = logFile()
    assert type(x) == str