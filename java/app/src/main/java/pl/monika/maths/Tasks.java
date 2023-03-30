package pl.monika.maths;

import android.content.res.Resources;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;

public class Tasks {
    public static String[] tasks;

    public static void init(Resources res){
        // read from file
        String a = readResource(res, R.raw.operations);
        // split by end of line
        tasks = a.split("\r?\n|\r");
    }

    public static String yourTask(){
        int min = 0;
        int max = tasks.length;
        int r = (int) (Math.random()*(max-min)) + min;
        int x = randDigit(1);
        int y = randDigit(1);
        int z = randDigit(1);
        String t = tasks[r];

        t = t.replace("x", Integer.toString(x)).replace("y", Integer.toString(y))
                .replace("z", Integer.toString(z));
        return t;
    }

    public static int randDigit(int min){
        int max = 5;
        int x = (int) (Math.random()*(max-min)) + min;
        return x;
    }



    public static String readResource(Resources res, int id) {
        InputStream input = res.openRawResource(id);
        try {
            byte[] b = new byte[input.available()];
            input.read(b);
            return new String(b);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}
