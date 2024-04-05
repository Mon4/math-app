package pl.monika.maths;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
    }

    public void launchToMode(View v){
        Intent myIntent = new Intent(this, MenuActivity2.class);
        startActivity(myIntent);
    }

    public void launchToSettings(View v){
        Intent myIntent = new Intent(this, SettingsActivity.class);
        startActivity(myIntent);
    }
    public void exit (View v){
        this.finishAffinity();
    }


}