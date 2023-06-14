/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年3月28日
 */
public class P3 {
    public static void main(String[] args) {
        final int NUM = 4;
        for(int i = 0; i < NUM; i++) {
            for(int j = 0; j < NUM - i; j++) {
                System.out.print(" ");
            }
            for(int j = 0; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
