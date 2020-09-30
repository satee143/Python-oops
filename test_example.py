#contentoftest_example.py
import pytest

@pytest.fixture
def error_fixture():
	assert 0 
def test_ok():
	print("ok")
	
def test_fail():
	assert 0
	
def test_error(error_fixture):
	pass
def test_skip():
	pytest.skip("skippingthistest")
	
def test_xfail():
	pytest.xfail('failing test case')

pytest.mark.xfail(reason='always xfail')
def test_xpass():
	pass