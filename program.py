from dna_database import DnaDatabase

if __name__ == '__main__':

    ''' Expected output:
            Match: Bob
            Match: None
            Match: Alice
    '''
    samples = [
        'AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG',
        'CGCAAAGACTTTATTGCGCCCACAGTGGCTTTTGTCTACTGATTCCATAGATAATGACAAATGTTCAAGGGGTTCTGGTACTTAGTCCGATCTCAGTGCGACTCGGGGGCGAACGTCGTGGTTATAAACTCGTCCAGATGCCGGCGCCAAACAAATATGATCCCATTGTGCACCCCCACTGGTCAGAACTCTCGGTGCTTAAGCGATACACGCGTCCGTGAGCATTCAACACCCAACTACTAGTCCGGTAATCTGAATGCACACGTGGCCCGGGTTACCGGGATGCCGAAAGAAAGAAAG',
        'GGGGAATATGGTTATTAAGTTAAAGAGAAAGAAAGATGTGGGTGATATTAATGAATGAATGAATGAATGAATGAATGAATGTTATGATAGAAGGATAAAAATTAAATAAAATTTTAGTTAATAGAAAAAGAATATATAGAGATCAGATCTATCTATCTATCTTAAGGAGAGGAAGAGATAAAAAAATATAATTAAGGAA' 
    ]

    dna_database = DnaDatabase('./data/small.csv')

    for sample in samples:
        match = dna_database.find_match(sample)
        print(f'Match: {match}')
