package P3;

/**
 * 饭卡
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月04日
 */
public class MealCard implements BaseThing {
    /**
     * 事物名称 - 饭卡
     */
    private String name;

    public MealCard(String name) {
        this.name = name;
    }

    @Override
    public void doSomething(String personName) {
        System.out.printf("%s用%s刷卡吃饭%n", personName, this.name);
    }

}
