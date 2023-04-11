package P1;

/**
 * 交通工具类
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月04日
 */
public class Vehicle {
    /**
     * 速度
     */
    private double speed;

    /**
     * 行驶距离
     */
    private double dist;

    /**
     * 行驶时间
     */
    private double time;

    /**
     * 驾驶证分数
     */
    private int license = 12;

    public int getLicense() {
        return license;
    }

    public void setLicense(int license) {
        this.license = license;
    }

    public Vehicle(double speed) {
        this.speed = speed;
    }

    /**
     * 加速
     * 
     * @param speed 加速后的速度
     */
    public void speedUp(double speed) {
        this.speed = speed;
    }

    /**
     * 行驶
     * 
     * @param time 行驶时间
     */
    public void drive(double time) {
        this.time = time;
        this.dist += this.time * this.speed;
    }

    /**
     * 显示信息
     */
    public void showInfo() {
        System.out.println("此辆车行驶了" + this.dist + "公里");
    }
}
