package P2;

import java.awt.Rectangle;

/**
 * custom Rectangle
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月11日
 */
public class MyRectangle {

    public static void main(String[] args) {
        // test1();
        test2();
    }

    /**
     * 需求一：生成两个指定坐标、指定宽度的长方形，显示长方形信息。
     */
    public static void test1() {
        int x = 10;
        int y = 10;
        int width = 10;
        int height = 5;
        Rectangle rectangle = new Rectangle(x, y, width, height);
        showInfo(rectangle);
    }

    public static void showInfo(Rectangle rectangle) {
        System.out.printf("长方形的左上角坐标是(%s, %s), 宽度width = %s, 高度height = %s%n",
                rectangle.getX(), rectangle.getY(), rectangle.getWidth(), rectangle.getHeight());
    }

    /**
     * 需求二：返回两个长方形相交形成的长方形，并计算该长方形的面积
     */
    public static void test2() {
        int width1 = 10;
        int height1 = 8;
        // 长方形一
        Rectangle rectangle1 = new Rectangle(width1, height1);
        int x2 = 5;
        int y2 = 6;
        int width2 = 15;
        int height2 = 7;
        // 长方形二
        Rectangle rectangle2 = new Rectangle(x2, y2, width2, height2);

        if (!rectangle1.intersects(rectangle2)) {
            System.out.println("两个长方形没有交集！");
        }
        // 得到二者相交的长方形
        Rectangle intersection = rectangle1.intersection(rectangle2);
        // 计算面积
        double width = intersection.getWidth();
        double height = intersection.getHeight();
        System.out.printf("长方形面积Size = %s%n", width * height);
    }

}
