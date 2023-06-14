package P1;

import java.awt.event.*;
import javax.swing.*;

/**
 * 
 * @author codejuzi
 * @CreatedTime 2023年4月23日
 */
public class MyListener implements ActionListener {

    JLabel l;
    JTextField t;

    MyListener(JLabel jl, JTextField jt) {
        this.l = jl;
        this.t = jt;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        this.l.setText(t.getText());
    }
}