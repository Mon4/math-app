package pl.monika.maths;
import android.content.res.Resources;
import java.io.IOException;
import java.io.InputStream;
import java.util.Stack;

public class Tasks {
    public static String[] tasks;

    public static void init(Resources res){
        // read from file
        String a = readResource(res, R.raw.operations);
        // split by end of line
        tasks = a.split("\r?\n|\r");
    }

    public static Task yourTask(){
        int res;
        String t = "";
        String task = "";
        do  {
            int min = 0;
            int max = tasks.length;
            int r = (int) (Math.random()*(max-min)) + min;
            int x = randDigit(1);
            int y = randDigit(1);
            int z = randDigit(1);

            t = tasks[r];

            task = t.replace("x", Integer.toString(x)).replace("y", Integer.toString(y))
                    .replace("z", Integer.toString(z));

            if (t.equals("x / y")){
                int temp = x * y;
                y = x;
                x = temp;
                task = x + " / " + y;
            }

            res = eval_task(task);
        } while (res < 0);

        Task ta = new Task (task, res);
        return ta;
    }



    public static int randDigit(int min){
        int max = 5;
        int x = (int) (Math.random()*(max-min)) + min;
        return x;
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

    public static int stackToInt(Stack<Integer> stack) {
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
