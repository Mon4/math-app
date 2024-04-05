package pl.monika.maths;

import android.content.SharedPreferences;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.preference.ListPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceManager;

public class SettingsActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        // to check if frame layout is empty or not
        if (findViewById(R.id.idFrameLayout) != null) {
            if (savedInstanceState != null) {
                return;
            }
            // to inflate our fragment.
            getFragmentManager().beginTransaction().add(R.id.idFrameLayout, new SettingsFragment()).commit();
        }

        SharedPreferences mSharedPreferences = PreferenceManager.getDefaultSharedPreferences(this);
//      String b = getResources().getString(R.string.default_pref_value);
        String[] a = getResources().getStringArray(R.array.levels);
        int c = Integer.parseInt(mSharedPreferences.getString("difficulty_level_key", "1"));
        String g = a[c];


    }
}