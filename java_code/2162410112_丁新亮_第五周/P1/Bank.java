package P1;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月25日
 */
public class Bank {
    /**
     * 余额
     */
    private double account;

    public Bank(double account) {
        this.account = account;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new BankException("额度异常");
        }
        this.account += amount;
        System.out.println("剩余: ￥" + this.account);
    }

    public void withdraw(double amount) throws BankException {
        if (this.account <= 0 || this.account < amount) {
            throw new BankException("余额不足");
        } else if (amount > 1000) {
            throw new BankException("超出额度");
        }
        this.account -= amount;
        System.out.println("剩余: ￥" + this.account);
    }
}
