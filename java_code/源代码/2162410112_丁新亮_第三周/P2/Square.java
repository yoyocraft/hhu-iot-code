package P2;

import java.awt.Rectangle;

/**
 * 需求三：继承Rectangle，创建Square（正方形），自行修改构造方法，添加可以获取对角线长度的成员方法
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月11日
 */
public class Square extends Rectangle {

    public Square(int width) {
        super(width, width);
        this.width = width;
        this.height = width;
    }

    /**
     * 获取对角线长度
     * 
     * @return 对角线长度
     */
    public double getDiagonalLength() {
        return Math.sqrt(this.width * this.width * 2);
    }


    public static void main(String[] args) {
        Square square = new Square(10);
        double diagonalLength = square.getDiagonalLength();
        System.out.println("diagonal length = " + diagonalLength);
    }
}
