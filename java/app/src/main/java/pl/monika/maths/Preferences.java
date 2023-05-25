package pl.monika.maths;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.res.Resources;

import androidx.preference.PreferenceManager;

public class Preferences {

    public static String getDifficulty(Resources res, Context context) {
        SharedPreferences mSharedPreferences = PreferenceManager.getDefaultSharedPreferences(context);
        String[] a = res.getStringArray(R.array.levels);

        int c = Integer.parseInt(mSharedPreferences.getString("difficulty_level_key", "1"));
        String g = a[c];
        return g;
    }
}
