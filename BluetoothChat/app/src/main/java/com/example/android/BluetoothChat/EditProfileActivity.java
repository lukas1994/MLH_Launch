package com.example.android.BluetoothChat;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.widget.Button;

/**
 * Created by Joshua on 04/10/14.
 */

public class EditProfileActivity extends Activity implements View.OnClickListener {

    public static final int IMAGE_PICKER_SELECT = 1;



    @Override
    public void onClick(View view) {

        switch(view.getId()){
            case R.id.select_picture_button:
                Intent i = new Intent(Intent.ACTION_PICK, android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
                startActivityForResult(i, IMAGE_PICKER_SELECT);
        }

    }

    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        switch(requestCode){
            case IMAGE_PICKER_SELECT:
                Uri selectedImageUri = data.getData();
                Log.e("Edit", selectedImageUri.toString());
                break;
        }
    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Setup the window
        requestWindowFeature(Window.FEATURE_INDETERMINATE_PROGRESS);
        setContentView(R.layout.edit_profile);

        Button pictureButton = (Button) findViewById(R.id.select_picture_button);
        pictureButton.setOnClickListener(this);


        //
    }
}
