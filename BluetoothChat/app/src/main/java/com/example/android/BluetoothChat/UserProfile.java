package com.example.android.BluetoothChat;

import android.media.Image;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

/**
 * Created by Joshua on 04/10/14.
 */
public class UserProfile implements Serializable {
    private String name;
    private String dp;
    private boolean gender;
    private int age;
    private String bio;

    UserProfile(String name, String dp, boolean gender, int age, String bio) {
        setAge(age);
        setName(name);
        setBio(bio);
        setDp(dp);
        setGender(gender);

    }

    //getter methods
    public String getName() {
    return this.name;
    }
    public boolean getGender() {
        return this.gender;
    }
    public int getAge() {
            return this.age;
    }
    public String getBio() {
        return this.bio;
    }
    public String getDp() {
        return this.dp;
    }

    //Setter methods
    public void setName(String name) {
        this.name = name;
    }

    public void setGender(boolean gender) {
        this.gender = gender;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }

    public void setDp(String dp) {

    }

    //Implementing serializable methods

    private void readObject(ObjectInputStream aInputStream)
    throws IOException, ClassNotFoundException {
        aInputStream.defaultReadObject();
    }

    private void writeObject(ObjectOutputStream aOutputStream)
    throws IOException {
        aOutputStream.defaultWriteObject();
    }

}
