package pl.monika.maths;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.gson.Gson;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.ResponseBody;

public class MainActivity extends AppCompatActivity {
    public static final MediaType MEDIA_TYPE_PNG = MediaType.get("image/png; charset=utf-8");
    static OkHttpClient client = new OkHttpClient();
    String task;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Tasks.init(getResources());

        TextView mTextView = findViewById(R.id.text_task);
        task = Tasks.yourTask();
        mTextView.setText(task);

        View view = this.getWindow().getDecorView();
        view.setBackgroundColor(Color.GRAY);

    }

    public void clean (View v){
        PaintView x = findViewById(R.id.paintView);
        x.clearCanvas();
    }

    public void send (View v) throws IOException {
        PaintView x = findViewById(R.id.paintView);
        byte[] bmp = x.viewToBitmap();

        RequestBody requestBody = new MultipartBody.Builder()
                .setType(MultipartBody.FORM)
                .addFormDataPart("file", "logo-square.png",
                        RequestBody.create(bmp, MEDIA_TYPE_PNG))
                .build();

        Request request = new Request.Builder()
                .url("https://guarded-island-03261.herokuapp.com/predict")
                .post(requestBody)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
                try (ResponseBody responseBody = response.body()) {
                    if (!response.isSuccessful())
                        throw new IOException("Unexpected code " + response);
                    NumberResult result;
                    String str = responseBody.string();
                    Gson g = new Gson();
                    result = g.fromJson(str, NumberResult.class);
                    if (result.prediction != null) {
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                TextView y = findViewById(R.id.text_answer);
                                y.setText(result.prediction.toString());
                            }
                        });
                        System.out.println(result.prediction);
                    }
                }
            }

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }
    });
}
    public void check (View v){
        TextView mTextView = findViewById(R.id.text_result);
        mTextView.setText(Tasks.eval_task(task));

    }


}