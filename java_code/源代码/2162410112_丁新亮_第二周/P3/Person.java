package P3;

/**
 * 本人类
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月04日
 */
public class Person {

    /**
     * 姓名
     */
    private String name;

    /**
     * 兴趣
     */
    private String hobby;


    public Person(String name, String hobby) {
        this.name = name;
        this.hobby = hobby;
    }


    /**
     * 本人类可以做的行为
     */
    public void doPersonThing() {
        System.out.println(this.name + "在学习");
    }

    /**
     * 
     */
    public void doSomethingWithBaseThing(BaseThing baseThing) {
        baseThing.doSomething(this.name);
    }


    @Override
    public String toString() {
        return "Person [name=" + name + ", hobby=" + hobby + "]";
    }

}
