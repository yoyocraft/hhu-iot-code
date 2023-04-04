package P3;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月04日
 */
public class Test {
    public static void main(String[] args) {
        Person person = new Person("CodeJuzi", "逛逛GitHub，参与开源");
        person.doPersonThing();
        person.doSomethingWithBaseThing(new MealCard("河海校园饭卡"));
        person.doSomethingWithBaseThing(new Phone("小米手机"));
    }
}
