package P2;

import javax.swing.*;

/**
 * 计算器类
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月23日
 */
public class Calculator {

    private final JTextField input1;
    private final JTextField input2;
    private final JButton addBtn;
    private final JButton subBtn;
    private final JButton mulBtn;
    private final JButton divBtn;
    private final JLabel resLabel;

    public Calculator() {
        // init ui
        JFrame frame = new JFrame("Calculator");
        frame.setSize(400, 250);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // create input frame and button
        this.input1 = new JTextField(10);
        this.input2 = new JTextField(10);
        addBtn = new JButton("+");
        subBtn = new JButton("-");
        mulBtn = new JButton("*");
        divBtn = new JButton("/");
        resLabel = new JLabel("Result = ");

        // create layout
        JPanel panel = new JPanel();
        panel.add(new JLabel("num1 = "));
        panel.add(input1);
        panel.add(new JLabel("num2 = "));
        panel.add(input2);
        panel.add(addBtn);
        panel.add(subBtn);
        panel.add(mulBtn);
        panel.add(divBtn);
        panel.add(resLabel);

        // set listeners and calculator button
        addListeners();
        // add layout in windows
        frame.add(panel);

        // show windows
        frame.setVisible(true);
    }

    /**
     * 添加监听器
     */
    private void addListeners() {
        addBtn.addActionListener(e -> {
            try {
                double num1 = Double.parseDouble(input1.getText());
                double num2 = Double.parseDouble(input2.getText());
                double res = num1 + num2;
                resLabel.setText("res = " + res);
            } catch (NumberFormatException ex) {
                resLabel.setText("大哥，这里是计算器，你输入个不是数字的东东是个啥意思？？");
                System.out.println(ex.getMessage());
            }
        });

        subBtn.addActionListener(e -> {
            try {
                double num1 = Double.parseDouble(input1.getText());
                double num2 = Double.parseDouble(input2.getText());
                double res = num1 - num2;
                resLabel.setText("res = " + res);
            } catch (NumberFormatException ex) {
                resLabel.setText("大哥，这里是计算器，你输入个不是数字的东东是个啥意思？？");
                System.out.println(ex.getMessage());
            }
        });

        mulBtn.addActionListener(e -> {
            try {
                double num1 = Double.parseDouble(input1.getText());
                double num2 = Double.parseDouble(input2.getText());
                double res = num1 * num2;
                resLabel.setText("res = " + res);
            } catch (NumberFormatException ex) {
                resLabel.setText("大哥，这里是计算器，你输入个不是数字的东东是个啥意思？？");
                System.out.println(ex.getMessage());
            }
        });

        divBtn.addActionListener(e -> {
            try {
                double num1 = Double.parseDouble(input1.getText());
                double num2 = Double.parseDouble(input2.getText());
                double res = num1 / num2;
                resLabel.setText("res = " + res);
            } catch (NumberFormatException ex) {
                resLabel.setText("大哥，这里是计算器，你输入个不是数字的东东是个啥意思？？");
                System.out.println(ex.getMessage());
            }
        });

    }

    public static void main(String[] args) {
        new Calculator();
    }
}
