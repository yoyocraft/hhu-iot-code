package P2;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月04日
 */
public class Test {
    public static void main(String[] args) {
        Vehicle vehicle = new Vehicle(10);
        vehicle.drive(10);
        vehicle.speedUp(15);
        vehicle.drive(15);
        vehicle.showInfo();
    }
}
