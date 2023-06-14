package P1;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月25日
 */
public class Test {
    public static void main(String[] args) {
        Bank myBank = new Bank(1000.0);

        try {
            // 正常取款
            myBank.withdraw(500.0);
            // 取款超出额度
            myBank.withdraw(2000.0);
        } catch (BankException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            myBank.deposit(-500.0); // 存款为负数
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
