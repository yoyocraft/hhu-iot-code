import java.io.IOException;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月04日
 */
public class P1 {

    public static void main(String[] args) throws IOException {
        int a = (int) System.in.read() - '0';
        char b = (char) System.in.read();
        int c = (int) System.in.read() - '0';
        int res = 0;
        switch (b) {
            case '+':
                res = add(a, c);
                break;
            case '-':
                res = sub(a, c);
                break;
            case '*':
                res = mul(a, c);
                break;
            case '/':
                res = div(a, c);
                break;
            default:
        }
        System.out.println("res = " + res);
    }

    public static int add(int a, int b) {
        return a + b;
    }

    public static int sub(int a, int b) {
        return a - b;
    }

    public static int mul(int a, int b) {
        return a * b;
    }

    public static int div(int a, int b) {
        return (int) (a / b);
    }
}
