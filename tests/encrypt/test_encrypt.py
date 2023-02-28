from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("encryptmessage", "test")
    assert encrypt_message("encryptmessage", 2) == "egassemtpyrc_ne"
    assert encrypt_message("encryptmessage", 3) == "cne_egassemtpyr"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(["encryptmessagem"], 4)
    assert encrypt_message("encryptmessage", 5) == "yrcne_egassemtp"
    assert encrypt_message("encryptmessage", 2345) == "egassemtpyrcne"
    