package P1;

/**
 * 摩托车类
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月11日
 */
public class Bike extends Vehicle {

    /**
     * 最大速度
     */
    private int maxSpeed = 50;

    public Bike(double speed) {
        super(speed);

    }

    @Override
    public void speedUp(double speed) {
        super.speedUp(speed);
        if (speed > maxSpeed) {
            System.out.println("超速！");
            this.setLicense(this.getLicense() - 3);
        }
    }

    @Override
    public void showInfo() {
        super.showInfo();
        System.out.printf("驾驶证剩余分数 License = %d分%n", this.getLicense());
    }
}
