package P2;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月25日
 */
public class Test {
    public static void main(String[] args) {
        Bank bank = new Bank(0.0);
        Husband husband = new Husband(bank);
        Wife wife = new Wife(bank);
        
        new Thread(husband).start();
        new Thread(wife).start();
    }
}
