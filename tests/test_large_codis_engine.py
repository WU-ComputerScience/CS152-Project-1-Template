
from dna_database import DnaDatabase

expected_matches = {
        '1' : 'None',
        '2' : 'None',
        '3' : 'None',
        '4' : 'None',
        '5' : 'Lavender',
        '6' : 'Luna',
        '7' : 'Ron',
        '8' : 'Ginny',
        '9' : 'Draco',
        '10' : 'Albus',
        '11' : 'Hermione',
        '12' : 'Lily',
        '13' : 'None',
        '14' : 'Severus',
        '15' : 'Sirius',
        '16' : 'None',
        '17' : 'Harry',
        '18' : 'None',
        '19' : 'Fred',
        '20' : 'None'
    }

dna_database = DnaDatabase('data/large.csv')

def get_testdna_sample(num: int) -> str:
    path = os.path.join('test_dna_samples', f'{str(num)}.txt')
    with open(path, 'r') as file:
        return file.readline()
    
def test_large_01_should_match_none():
    '''Test Sequence #1 in Large Database Should Match None'''
    # Arrange
    test_number = '1'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_02_should_match_none():
    '''Test Sequence #2 in Large Database Should Match None'''
    # Arrange
    test_number = '2'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_03_should_match_none():
    '''Test Sequence #3 in Large Database Should Match None'''
    # Arrange
    test_number = '3'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_04_should_match_none():
    '''Test Sequence #4 in Large Database Should Match None'''
    # Arrange
    test_number = '4'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_05_should_match_lavender():
    '''Test Sequence #5 in Large Database Should Match Lavender'''
    # Arrange
    test_number = '5'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_06_should_match_luna():
    '''Test Sequence #6 in Large Database Should Match Luna'''
    # Arrange
    test_number = '6'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_07_should_match_ron():
    '''Test Sequence #7 in Large Database Should Match Ron'''
    # Arrange
    test_number = '7'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_08_should_match_ginny():
    '''Test Sequence #4 in Large Database Should Match Ginny'''
    # Arrange
    test_number = '8'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_09_should_match_draco():
    '''Test Sequence #4 in Large Database Should Match Draco'''
    # Arrange
    test_number = '9'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_10_should_match_albus():
    '''Test Sequence #10 in Large Database Should Match Albus'''
    # Arrange
    test_number = '10'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_11_should_match_hermione():
    '''Test Sequence #11 in Large Database Should Match Hermione'''
    # Arrange
    test_number = '11'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_12_should_match_lily():
    '''Test Sequence #12 in Large Database Should Match Lily'''
    # Arrange
    test_number = '12'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_13_should_match_none():
    '''Test Sequence #13 in Large Database Should Match None'''
    # Arrange
    test_number = '13'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_14_should_match_severus():
    '''Test Sequence #14 in Large Database Should Match Severus'''
    # Arrange
    test_number = '14'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_15_should_match_sirius():
    '''Test Sequence #14 in Large Database Should Match Sirius'''
    # Arrange
    test_number = '15'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_16_should_match_none():
    '''Test Sequence #16 in Large Database Should Match None'''
    # Arrange
    test_number = '16'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_17_should_match_harry():
    '''Test Sequence #17 in Large Database Should Match Harry'''
    # Arrange
    test_number = '17'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_18_should_match_none():
    '''Test Sequence #18 in Large Database Should Match None'''
    # Arrange
    test_number = '18'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_19_should_match_fred():
    '''Test Sequence #19 in Large Database Should Match Fred'''
    # Arrange
    test_number = '19'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]

def test_large_20_should_match_none():
    '''Test Sequence #20 in Large Database Should Match None'''
    # Arrange
    test_number = '20'
    testdna_sample = get_testdna_sample(test_number)

    # Act
    match = dna_database.find_match(testdna_sample)

    # Assert
    assert match == expected_matches[test_number]
