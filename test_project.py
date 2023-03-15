from project import check_command_line_arg,select_department,select_currentyear
import pytest
def test_check_command_line_arg():
    with pytest.raises(SystemExit):
        check_command_line_arg()


def test_department():
    assert select_department("Web Development")== "IT "
    assert select_department("Mobile Computing")== "CSE "
    assert select_department("Home Automation")== "EEE "
    assert select_department("Integrated Circuit")== "ECE "

def test_currentyear():
    assert select_currentyear(2019)== "year1"
    assert select_currentyear(2020)== "year2"
    assert select_currentyear(2021)== "year3"
    assert select_currentyear(2022)== "year4"