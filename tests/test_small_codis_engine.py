import os
from dna_database import DnaDatabase

                          
expected_matches = {
        '1' : 'Bob',
        '2' : 'None',
        '3' : 'None',
        '4' : 'Alice',
        '5' : 'None',
        '6' : 'None',
        '7' : 'None',
        '8' : 'None',
        '9' : 'None',
        '10' : 'None',
        '11' : 'None',
        '12' : 'None',
        '13' : 'None',
        '14' : 'None',
        '15' : 'None',
        '16' : 'None',
        '17' : 'None',
        '18' : 'None',
        '19' : 'None',
        '20' : 'None'
    }
dna_database = DnaDatabase('data/small.csv')

def get_testdna_sample(num: int) -> str:
    path = os.path.join('test_dna_samples', f'{str(num)}.txt')
    with open(path, 'r') as file:
        return file.readline()
        
def test_small_01_should_match_bob():
    '''Test Sequence #1 in Small Database Should Match Bob'''
    # Arrange
    test_number = '1'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_02_should_match_none():
    '''Test Sequence #2 in Small Database Should Match None'''
    # Arrange
    test_number = '2'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_03_should_match_none():
    '''Test Sequence #3 in Small Database Should Match None'''
    # Arrange
    test_number = '3'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_04_should_match_alice():
    '''Test Sequence #4 in Small Database Should Match Alice'''
    # Arrange
    test_number = '4'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_05_should_match_none():
    '''Test Sequence #5 in Small Database Should Match None'''
    # Arrange
    test_number = '5'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_06_should_match_none():
    '''Test Sequence #6 in Small Database Should Match None'''
    # Arrange
    test_number = '6'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_07_should_match_none():
    '''Test Sequence #7 in Small Database Should Match None'''
    # Arrange
    test_number = '7'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_08_should_match_none():
    '''Test Sequence #4 in Small Database Should Match None'''
    # Arrange
    test_number = '8'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_09_should_match_none():
    '''Test Sequence #4 in Small Database Should Match None'''
    # Arrange
    test_number = '9'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_10_should_match_none():
    '''Test Sequence #10 in Small Database Should Match None'''
    # Arrange
    test_number = '10'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_11_should_match_none():
    '''Test Sequence #11 in Small Database Should Match None'''
    # Arrange
    test_number = '11'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_12_should_match_none():
    '''Test Sequence #12 in Small Database Should Match None'''
    # Arrange
    test_number = '12'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_13_should_match_none():
    '''Test Sequence #13 in Small Database Should Match None'''
    # Arrange
    test_number = '13'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_14_should_match_none():
    '''Test Sequence #14 in Small Database Should Match None'''
    # Arrange
    test_number = '14'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_15_should_match_none():
    '''Test Sequence #14 in Small Database Should Match None'''
    # Arrange
    test_number = '15'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_16_should_match_none():
    '''Test Sequence #16 in Small Database Should Match None'''
    # Arrange
    test_number = '16'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_17_should_match_none():
    '''Test Sequence #17 in Small Database Should Match None'''
    # Arrange
    test_number = '17'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_18_should_match_none():
    '''Test Sequence #18 in Small Database Should Match None'''
    # Arrange
    test_number = '18'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_19_should_match_none():
    '''Test Sequence #19 in Small Database Should Match None'''
    # Arrange
    test_number = '19'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_small_20_should_match_none():
    '''Test Sequence #20 in Small Database Should Match None'''
    # Arrange
    test_number = '20'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]
