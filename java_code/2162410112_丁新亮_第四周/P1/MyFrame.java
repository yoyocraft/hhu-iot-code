package P1;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月23日
 */
public class MyFrame extends JFrame {
    JLabel jl = new JLabel();

    JTextField jt = new JTextField(10);

    public MyFrame() {
        setLayout(new FlowLayout());

        JButton button = new JButton("Show");

        this.add(jt);
        this.add(button);
        this.add(jl);

        MyListener ml = new MyListener(jl, jt);

        button.addActionListener((ActionListener) ml);
    }
}