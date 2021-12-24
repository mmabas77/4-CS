package com.mmabas77.presenter;

import com.mmabas77.model.CaesarCipher;
import com.mmabas77.model.PlayfairCipher;
import com.mmabas77.model.TranspositionCipher;
import com.mmabas77.model.interfaces.Cipher;
import com.mmabas77.view.MainFrame;

public class MainPresenter {

    public void encrypt(String key, String message, Cipher.Type type) {
        try {
            Cipher cipher = getCipher(key, type);
            updateUI(cipher.encrypt(message));
        } catch (Exception ex) {
            showErrorMessage(ex);
        }
    }

    public void decrypt(String key, String message, Cipher.Type type) {
        try {

            Cipher cipher = getCipher(key, type);
            updateUI(cipher.decrypt(message));
        } catch (Exception ex) {
            showErrorMessage(ex);
        }
    }

    private void updateUI(String output) {
        this.frame.updateUI(output);
    }

    private void showErrorMessage(Exception ex) {
        this.frame.showErrorMessage(ex.getMessage());
    }

    private Cipher getCipher(String key, Cipher.Type type) {
        Cipher cipher;
        if (type == Cipher.Type.CAESAR_CIPHER)
            cipher = new CaesarCipher(Integer.valueOf(key));
        else if (type == Cipher.Type.PLAYFAIR_CIPHER)
            cipher = new PlayfairCipher(key);
        else if (type == Cipher.Type.TRANSPOSITION_CIPHER)
            cipher = new TranspositionCipher(key);
        else
            throw new IllegalArgumentException(
                    String.format("Type %s not implemented", type.name())
            );
        return cipher;
    }

    /*
    Singleton Class
     */
    private static MainPresenter instance = null;

    public static synchronized MainPresenter getInstance(MainFrame frame) {
        if (instance == null)
            instance = new MainPresenter(frame);
        return instance;
    }

    /*
        Construction Of OBJ
         */
    private MainFrame frame;

    private MainPresenter(MainFrame frame) {
        this.frame = frame;
    }

}
