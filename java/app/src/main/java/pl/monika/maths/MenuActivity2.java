package pl.monika.maths;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

public class MenuActivity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu2);

    }

    public void launchToOperations(View v) {
        String mode = "operations";
        Tasks.init(getResources(), Mode.operations);
        Intent myIntent = new Intent(this, MainActivity.class);
        startActivity(myIntent);

    }

    public void launchToAreas(View v){
        String mode = "areas";

//        Intent myIntent = new Intent(this, MainActivity.class);
//        startActivity(myIntent);
    }

    public void launchToText(View v){
        Tasks.init(getResources(), Mode.text);
        Intent myIntent = new Intent(this, MainActivity.class);
        startActivity(myIntent);
    }

}