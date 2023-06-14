package P2;

/**
 * @author codejuzi
 * @CreatedTime 2023年4月25日
 */
public class Bank {
    /**
     * 余额
     */
    private double account;

    private static final double MAX_WITHDRAW_MONEY = 1000;

    public Bank(double account) {
        this.account = account;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new BankException("额度异常");
        }
        this.account += amount;
        System.out.printf("存入￥%s, 余额为￥%s%n", amount, this.account);
    }

    public void withdraw(double amount) throws BankException {
        if (this.account <= 0 || this.account < amount) {
            throw new BankException("余额不足");
        } else if (amount > MAX_WITHDRAW_MONEY) {
            throw new BankException("超出额度");
        }
        this.account -= amount;
        System.out.printf("取出￥%s, 余额为￥%s%n", amount, this.account);
    }
}
