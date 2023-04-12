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

    public void launchToOperations(View v) {
        Intent myIntent = new Intent(this, MainActivity.class);
        startActivity(myIntent);
    }

    public void launchToAreas(View v){
//        Intent myIntent = new Intent(this, MainActivity.class);
//        startActivity(myIntent);
    }

    public void launchToText(View v){
//        Intent myIntent = new Intent(this, MainActivity.class);
//        startActivity(myIntent);
    }

    public void launchToSettings(View v){
//        Intent myIntent = new Intent(this, MainActivity.class);
//        startActivity(myIntent);
    }


}