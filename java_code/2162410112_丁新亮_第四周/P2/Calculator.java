package P2;

import javax.swing.*;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * 计算器类
 *
 * @author codejuzi
 * @CreatedTime 2023年4月23日
 */
public class Calculator extends JFrame implements ActionListener {

    private final JTextField input1;
    private final JTextField input2;
    private final JButton addBtn;
    private final JButton subBtn;
    private final JButton mulBtn;
    private final JButton divBtn;
    private final JLabel resLabel;

    public Calculator() {
        // init ui
        super("Calculator");
        this.setSize(400, 250);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

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
        addBtn.addActionListener(this);
        subBtn.addActionListener(this);
        mulBtn.addActionListener(this);
        divBtn.addActionListener(this);
        // add layout in windows
        this.add(panel);

        // show windows
        this.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        try {
            double num1 = Double.parseDouble(input1.getText());
            double num2 = Double.parseDouble(input2.getText());
            double result = 0;

            if (e.getSource().equals(addBtn)) {
                result = num1 + num2;
            } else if (e.getSource().equals(subBtn)) {
                result = num1 - num2;
            } else if (e.getSource().equals(mulBtn)) {
                result = num1 * num2;
            } else if (e.getSource().equals(divBtn)) {
                result = num1 / num2;
            }

            resLabel.setText("res = " + Double.toString(result));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Invalid input!");
        }
    }

    public static void main(String[] args) {
        new Calculator();
    }

}
