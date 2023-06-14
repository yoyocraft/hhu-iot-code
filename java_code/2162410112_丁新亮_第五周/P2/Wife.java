package P2;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月25日
 */
public class Wife extends Person {

    public Wife(Bank bank) {
        super(bank);
    }

    @Override
    protected double getAmount() {
        // 随机 0 ~ 1100
        return random.nextInt(1101);
    }

    @Override
    protected Runnable getTask() {
        return () -> {
            try {
                bank.withdraw(getAmount());
            } catch (BankException e) {
                e.printStackTrace();
            }
        };
    }
}
