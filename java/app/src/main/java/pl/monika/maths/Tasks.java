package pl.monika.maths;
import android.content.Context;
import android.content.res.Resources;
import androidx.annotation.NonNull;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Stack;

public class Tasks {
    public static ArrayList<Task> tasks;
    private static String pref;

    public Tasks(String pref) {
        Tasks.pref = pref;
    }

    public static void setPref(Resources res, Context context){
        Tasks.pref = Preferences.getDifficulty(res, context);
    }

    public static void init(Resources res, Context context, Mode mode){
        ArrayList<Task> list = new ArrayList<>();
        setPref(res, context);


        switch(mode) {
            case OPERATIONS:
                String a = readResource(res, R.raw.operations);
                String[] lines = a.split("\r?\n|\r");        // split by end of line
                for (String q : lines) {
                    Task task = new Task();
                    task.setEquation(q);
                    list.add(task);
                }
                break;

            case AREAS:
                String b = readResource(res, R.raw.areas);
                String[] lines2 = b.split("\r?\n|\r");

                for (int i=0; i<lines2.length; i+=2){
                    String e = lines2[i];
                    String q = lines2[i+1];
                    Task task = new Task();
                    task.setEquation(e);
                    task.setQuestion(q);
                    list.add(task);
                }
                break;

            case TEXT:
                String c = readResource(res, R.raw.text);
                String[] lines3 = c.split("\r?\n|\r");

                for (int i=0; i<lines3.length; i+=2){
                    String e = lines3[i];
                    String q = lines3[i+1];
                    Task task = new Task();
                    task.setEquation(e);
                    task.setQuestion(q);
                    list.add(task);
                }
                break;
        }
    tasks = list;
    }

    public static Task yourTask(Mode mode){
        int result;
        String equation = "";
        String operation = "";
        Task task;
        int x, y, z;

        int min = 0;
        int max = tasks.size();
        int r = (int) (Math.random()*(max-min)) + min;
        task = tasks.get(r);
        equation = task.equation;


        int max_digit = difficultyLevel(equation);

        do  {
            x = randDigit(1, max_digit);
            y = randDigit(1, max_digit);
            z = randDigit(1, max_digit);

            // divisible numbers
            if (equation.equals("x / y")){
                int temp = x * y;
                y = x;
                x = temp;
                operation = x + " / " + y;
            }
            else if(equation.equals("x * y / 2")){
                if (x * y % 2 != 0){
                    x += 1;
                }
            }

            operation = equation.replace("x", Integer.toString(x))
                    .replace("y", Integer.toString(y))
                    .replace("z", Integer.toString(z));


            result = eval_task(operation);
        } while (result < 0);


        // text mode - changes #x to numbers in questions
        if(mode.equals(Mode.TEXT) || mode.equals(Mode.AREAS)){
            String question = task.question;

            question = question.replace("#x", Integer.toString(x))
                    .replace("#y", Integer.toString(y))
                    .replace("#z", Integer.toString(z));

            task.setQuestion(question);
        }
        // for operations mode - sets operations as question
        else{
            task.setQuestion(operation);
        }

        task.setOperation(operation);
        task.setResult(result);

        return task;
    }



    public static int randDigit(int min, int max){
        int x = (int) (Math.random()*(max-min)) + min;
        return x;
    }

    public static int difficultyLevel(String equation){
        int max = 0;

        boolean containsStar = equation.contains("*");
        boolean containsSlash = equation.contains("/");

        // cases containing multiplying or dividing
        if (containsStar || containsSlash){
            switch (pref){
                case "łatwy":
                    max = 5;
                    break;
                case "średni":
                    max = 10;
                    break;
                case "trudny":
                    max = 20;
                    break;
            }
        }
        // cases with summing and subbing
        else{
            switch (pref){
                case "łatwy":
                    max = 10;
                    break;
                case "średni":
                    max = 50;
                    break;
                case "trudny":
                    max = 100;
                    break;
            }
        }
        return max;
    }


    public static Integer eval_task(String task) {
        String expression = task;
        Stack<Integer> stack = new Stack<>();
        int len = expression.length();
        char sign = 0;
        Integer operand1 = null;

        for (int i = 0; i < len; i++) {
            char ch = expression.charAt(i);

            if (ch == '+' || ch == '-' || ch == '*' || ch == '/') {
                // If the character is a sign
                sign = ch;
                operand1 = stackToInt(stack);
            }
            else if (Character.isDigit(ch)) {
                // If the character is a digit
                stack.push(Character.getNumericValue(ch));
            }

            if (i == len-1 || ch == ' ' && (sign != 0 && operand1 != null && stack.size() >= 1)){
                // if there are two numbers and sign between them then eval it
                int operand2 = stackToInt(stack);

                int result = 0;
                switch (sign) {
                    case '+':
                        result = operand1 + operand2;
                        break;
                    case '-':
                        result = operand1 - operand2;
                        break;
                    case '*':
                        result = operand1 * operand2;
                        break;
                    case '/':
                        result = operand1 / operand2;
                        break;
                }

                stack.push(result);
            }
        }
        return stackToInt(stack);
    }

    public static int stackToInt(@NonNull Stack<Integer> stack) {
        int result = 0;
        int multiplier = 1;
        while (!stack.isEmpty()) {
            int num = stack.pop();
            result += num * multiplier;
            multiplier *= 10;
        }
        return result;
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
