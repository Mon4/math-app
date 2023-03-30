package pl.monika.maths;

import android.content.res.Resources;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;

public class Tasks {
    public static String[] tasks;

    public static void init(Resources res){
        // read from file
        String a = readResource(res, R.raw.areas);
        // split by end of line
        tasks = a.split("\r?\n|\r");

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
