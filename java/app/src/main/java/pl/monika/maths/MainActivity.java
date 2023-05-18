package pl.monika.maths;

import android.content.Intent;
import android.content.SharedPreferences;
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
    Task task;
    private int task_counter = 1;
    private int good_counter = 0;
    String answer;
    Mode mode;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Intent intent = getIntent();
        mode = (Mode) intent.getSerializableExtra("mode");
        setContentView(R.layout.activity_main);

        TextView taskTextView = findViewById(R.id.text_task);
        task = Tasks.yourTask(mode);
        String question = task.question;
        taskTextView.setText(question);

        warmup();
    }

    public void clean (View v){
        PaintView x = findViewById(R.id.paintView);
        x.clearCanvas();
    }

    public void warmup(){
        Request request = new Request.Builder()
                .url("https://guarded-island-03261.herokuapp.com")
                .get()
                .build();
        client.newCall(request).enqueue(new Callback(){

            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
            }

            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
            }
        });
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
                    String str = responseBody.string();
                    answer = str.replace("\"", "").replace("\n", "").trim();
                    if (answer != null) {
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {
                                TextView y = findViewById(R.id.text_answer);
                                y.setText(answer);
                            }
                        });
                        System.out.println(answer);
                    }
                }
            }

            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }
    });
}
    public void check (View v) {
        TextView resultTV = findViewById(R.id.text_result);
        if (answer != null){
            if (answer.equals(task.result.toString())) {
                resultTV.setTextColor(this.getResources().getColor(R.color.green));
                resultTV.setText("DOBRZE !");
                good_counter += 1;
            } else {
                resultTV.setTextColor(this.getResources().getColor(R.color.red));
                resultTV.setText("ŹLE ! POPRAWNA ODP: " + task.result);
            }
        }
        else{
            resultTV.setTextColor(this.getResources().getColor(R.color.red));
            resultTV.setText("BRAK ODPOWIEDZI ! POPRAWNA ODP: " + task.result);
        }


        scoreUpdate();
    }

    public void next (View v) {
        TextView taskTV = findViewById(R.id.text_task);
        task = Tasks.yourTask(mode);
        String question = task.question;
        taskTV.setText(question);

        task_counter += 1;

        // cleaning
        TextView answerTV = findViewById(R.id.text_answer);
        answerTV.setText(R.string.answer);
        TextView resultTV = findViewById(R.id.text_result);
        resultTV.setTextColor(this.getResources().getColor(R.color.black));
        resultTV.setText(R.string.result);

        clean(v);
    }

    public void scoreUpdate() {
        TextView scoreTV = findViewById(R.id.text_score);
        scoreTV.setText("liczba punktów: " + good_counter + "/" + task_counter);
    }
}