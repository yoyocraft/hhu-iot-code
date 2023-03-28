import java.util.Scanner;


/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年3月28日
 */
public class P2 {
    private static final Scanner myScanner = new Scanner(System.in);

    public static void main(String[] args) {
        String s1 = "正常";
        String s2 = "违章";
        System.out.print("请输入速度：" );
        int speed = myScanner.nextInt();
        if(speed >= 60 && speed <= 120) {
            System.out.println(s1);
        } else {
            System.out.println(s2);
        }
    }
}
