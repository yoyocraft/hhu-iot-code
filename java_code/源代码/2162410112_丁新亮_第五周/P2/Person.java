package P2;

import java.util.Random;
import java.util.concurrent.*;

/**
 * @author codejuzi
 * @CreatedTime 2023年4月25日
 */
public abstract class Person implements Runnable {

    protected Bank bank;

    protected Random random;

    public Person(Bank bank) {
        this.bank = bank;
        this.random = new Random();
    }

    @Override
    public void run() {
        while (true) {
            // 核心线程数
            int corePollSize = 2;
            // 获取CPU盒数
            int maximumPoolSize = 5;
            // 存活时间
            int keepAliveTime = 3;
            // 创建线程
            ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(
                    corePollSize,
                    maximumPoolSize,
                    keepAliveTime,
                    TimeUnit.SECONDS,
                    new LinkedBlockingQueue<>(3),
                    Executors.defaultThreadFactory(),
                    new ThreadPoolExecutor.AbortPolicy());
            try {
                Thread.sleep(getInterval());
                // 执行任务
                threadPoolExecutor.execute(getTask());
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                // 关闭线程
                threadPoolExecutor.shutdown();
            }
        }
    }

    /**
     * @return 得到随机休眠时间（毫秒），默认1000ms
     */
    protected int getInterval() {
        return 1000;
    }

    /**
     * 根据运行绑定的对象不同， 获取存取金额
     *
     * @return 获得存取金额
     */
    protected abstract double getAmount();

    /**
     * 动态绑定，获取不同的线程任务（存取）
     *
     * @return 获得线程任务
     */
    protected abstract Runnable getTask();
}
