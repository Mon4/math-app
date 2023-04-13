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
        Mode mode = Mode.operations;
        Tasks.init(getResources(), mode);

        Intent i = new Intent(this, MainActivity.class);
        i.putExtra("mode", mode);

        startActivity(i);

    }

    public void launchToAreas(View v){
        Mode mode = Mode.text;
        Tasks.init(getResources(), mode);
//        Intent myIntent = new Intent(this, MainActivity.class);
//        startActivity(myIntent);
    }

    public void launchToText(View v){
        Mode mode = Mode.text;
        Tasks.init(getResources(), mode);

        Intent i = new Intent(this, MainActivity.class);
        i.putExtra("mode", mode);

        startActivity(i);
    }

}