from src.crypto import encrypt, decrypt, crack
import pytest



def test_encrypt_shift_1():
    actual = encrypt('abc',1)
    expected = 'bcd'
    assert actual == expected

def test_encrypt_shift_10():
    actual = encrypt('abc',10)
    expected = 'klm'
    assert actual == expected

def test_encrypt_all_uppercase():
    actual = encrypt('ALL UPPERCASE', 20)
    expected = 'UFF OJJYLWUMY'
    assert actual == expected

def test_decrypt_shift_1():
    encrypted = encrypt('abc', 1)
    actual = decrypt(encrypted, 1)
    expected = 'abc'
    assert actual == expected

def test_decrypt_shift_5():
    encrypted = encrypt('Welcome HOME', 5)
    actual = decrypt(encrypted, 5)
    expected = 'Welcome HOME'
    assert actual == expected

def test_encryption_upper_and_lower():
    actual = encrypt('Lets See How This Handles Uppercase And Lowercase', 7)
    expected = 'Slaz Zll Ovd Aopz Ohukslz Bwwlyjhzl Huk Svdlyjhzl'
    assert actual == expected

def test_encryption_with_non_alpha():
    actual = encrypt('!@# This msg has special --- characters!!', 15)
    expected = '!@# Iwxh bhv wph hetrxpa --- rwpgpritgh!!'
    assert actual == expected

def test_crack_without_knowing_shift():
    expected = 'It was the best of times, it was the worst of times.' 
    encrypted = encrypt(expected, 22)
    actual = crack(encrypted)
    assert actual == expected

def test_shift_wraps_around():
    actual = encrypt('abc',27)
    expected = 'bcd'
    assert actual == expected

def test_letter_wraps_around():
    actual = encrypt('zzz',1)
    expected = 'aaa'
    assert actual == expected