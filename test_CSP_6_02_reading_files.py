import CSP_6_02_reading_files as HW

def test_to_string():
    expected = "This is the text file\nFor the 6_02 homework\nThis is the longest line in the file\nGoodbye"
    result = HW.toString()
    assert result == expected

def test_longest_line():
    expected = "This is the longest line in the file\n"
    result = HW.longestLine()
    assert result == expected

def test_to_binary():
    expected = ["00011110","00010101","01001010","001001"]
    result = HW.toBinary()
    assert result == expected
