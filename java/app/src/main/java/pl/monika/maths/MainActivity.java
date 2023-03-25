package pl.monika.maths;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //PaintView paintView = new PaintView(this);
        //setContentView(paintView);

        View view = this.getWindow().getDecorView();
        view.setBackgroundColor(Color.GREEN);

    }
}