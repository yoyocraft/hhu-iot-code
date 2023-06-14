package P2;

/**
 * @author codejuzi
 * @CreatedTime 2023年4月25日
 */
public class Husband extends Person {

    public Husband(Bank bank) {
        super(bank);
    }

    @Override
    protected double getAmount() {
        return 5000.0;
    }

    @Override
    protected Runnable getTask() {
        return () -> bank.deposit(getAmount());
    }

    @Override
    protected int getInterval() {
        // 随机 0 ~ 5秒
        return random.nextInt(5001);
    }
}
