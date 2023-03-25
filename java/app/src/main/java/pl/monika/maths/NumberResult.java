package pl.monika.maths;

import java.util.Map;

public class NumberResult {
    public NumberResult(Map<String, Integer> prediction) {
        this.prediction = prediction;
    }

    public Map<String, Integer> prediction;
}
