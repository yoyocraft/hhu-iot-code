package P1;

/**
 * 测试类
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月11日
 */
public class Test {

    public static void main(String[] args) {
        testCar();
        testBike();
    }

    public static void testCar() {
        Vehicle car = new Car(60);
        car.drive(10);
        car.speedUp(120);
        car.drive(10);
        car.showInfo();
    }

    public static void testBike() {
        Vehicle bike = new Bike(30);
        bike.drive(10);
        bike.speedUp(60);
        bike.drive(10);
        bike.speedUp(70);
        bike.drive(10);
        bike.showInfo();
    }
}
