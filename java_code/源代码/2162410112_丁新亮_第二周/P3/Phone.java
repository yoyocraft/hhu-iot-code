package P3;

/**
 * 手机类
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月04日
 */
public class Phone implements BaseThing{
    /**
     * 事物名称 - 手机
     */
    private String name;

    public Phone(String name) {
        this.name = name;
    }

    @Override
    public void doSomething(String personName) {
        System.out.printf("%s用%s听音乐", personName, this.name);
    }

}
