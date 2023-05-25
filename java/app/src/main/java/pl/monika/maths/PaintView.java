package pl.monika.maths;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.PorterDuff;
import android.graphics.PorterDuffXfermode;
import android.util.AttributeSet;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup.LayoutParams;

import androidx.annotation.Nullable;

import java.io.ByteArrayOutputStream;
import java.util.ArrayList;
import java.util.List;

public class PaintView extends View {

    public LayoutParams params;
    public Path path = new Path();
    public List<Path> paths;
    private List<Integer> colors;
    private Paint brush = new Paint();
    private boolean cc;
    private int currentColor = Color.BLACK;


    public PaintView(Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);

        paths = new ArrayList<>();
        colors = new ArrayList<>();

        setupBrush();

        setBackgroundColor(Color.WHITE);


        params = new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT);
    }

    private void setupBrush(){
        brush.setColor(currentColor);
        brush.setAntiAlias(true);
        brush.setStrokeWidth(15);
        brush.setStyle(Paint.Style.STROKE);
        brush.setStrokeJoin(Paint.Join.ROUND);
    }


    @Override
    public boolean onTouchEvent(MotionEvent event){
        float pointX = event.getX();
        float pointY = event.getY();

        switch(event.getAction()){
            case MotionEvent.ACTION_DOWN:
                Path path = new Path();
                path.moveTo(pointX, pointY);
                paths.add(path);
                colors.add(currentColor);
                return true;
            case MotionEvent.ACTION_MOVE:
                paths.get(paths.size() - 1).lineTo(pointX, pointY);
                break;
            default:
                return false;
        }

        postInvalidate();
        return false;
    }

    @Override
    protected void onDraw(Canvas canvas) {



        for (int i = 0; i<paths.size(); i++){
            brush.setColor(colors.get(i));
            canvas.drawPath(paths.get(i), brush);
        }

        if (cc) {
            paths.clear();
        }

//        if (cc) {
//            path = new Path();
//            Paint clearPaint = new Paint();
//            clearPaint.setXfermode(new PorterDuffXfermode(PorterDuff.Mode.CLEAR));
//            canvas.drawRect(0, 0, 0, 0, clearPaint);
//            cc = false;
//        }
//        canvas.drawPath(path, brush);
    }

    public void clearCanvas()
    {
        cc =true;
        invalidate();
    }

    public byte[] viewToBitmap() {
        View view = this;
        Bitmap bitmap = Bitmap.createBitmap(view.getWidth(), view.getHeight(), Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bitmap);
        view.draw(canvas);

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream);
        byte[] byteArray = stream.toByteArray();
        bitmap.recycle();

        return byteArray;
    }

    public void DrawMode() {
        currentColor = Color.BLACK;

    }

    public void EraseMode() {
        currentColor = Color.WHITE;
    }


}
