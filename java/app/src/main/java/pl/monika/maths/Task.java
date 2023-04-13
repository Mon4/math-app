package pl.monika.maths;

public class Task {
    String equation;
    String operation;
    String question;
    Integer result;

//    public Task(String q) {
//        equation = q;
//    }
//
//    public Task(String e, int res) {
//        equation = e;
//        result = res;
//    }
//    public Task(String e, String question, int res) {
//        equation = e;
//        question = question;
//        result = res;
//    }

    public void setEquation(String equation) {
        this.equation = equation;
    }
    public void setOperation(String operation) {
        this.operation = operation;
    }
    public void setQuestion(String question) {
        this.question = question;
    }
    public void setResult(int result) {
        this.result = result;
    }

}
