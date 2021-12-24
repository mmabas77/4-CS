package com.mmabas77.model.interfaces;

public interface Cipher {

    String encrypt(String message);

    String decrypt(String message);
    enum Type {
        CAESAR_CIPHER,
        PLAYFAIR_CIPHER,
        TRANSPOSITION_CIPHER
    }
}
