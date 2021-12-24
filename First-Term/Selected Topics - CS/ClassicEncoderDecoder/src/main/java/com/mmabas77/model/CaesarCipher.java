package com.mmabas77.model;

import com.mmabas77.model.interfaces.Cipher;

public class CaesarCipher implements Cipher {

    private final int shift;

    public CaesarCipher(int shift) {
        this.shift = shift;
    }

    private String getDecryptedMessage(String message) {
        return new CaesarCipher(26 - this.shift).getEncryptedMessage(message);
    }

    private String getEncryptedMessage(String message) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < message.length(); i++) {
            if (Character.isUpperCase(message.charAt(i))) {
                char ch = (char) (((int) message.charAt(i) +
                        shift - 65) % 26 + 65);
                result.append(ch);
            } else {
                char ch = (char) (((int) message.charAt(i) +
                        shift - 97) % 26 + 97);
                result.append(ch);
            }
        }
        return result.toString();
    }

    @Override
    public String encrypt(String message) {
        return this.getEncryptedMessage(message);
    }

    @Override
    public String decrypt(String message) {
        return this.getDecryptedMessage(message);
    }
}
