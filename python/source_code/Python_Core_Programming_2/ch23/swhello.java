import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.lang.*;

public class swhello extends JFrame {
    JPanel box;
    JLabel hello;
    JButton quit;

    public swhello() {
        super("JSwing");
        JPanel box = new JPanel(new BorderLayout());
        JLabel hello = new JLabel("Hello World!");
        JButton quit = new JButton("QUIT");

        ActionListener quitAction = new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        };
        quit.setBackground(Color.red);
        quit.setForeground(Color.white);
        quit.addActionListener(quitAction);
        box.add(hello, BorderLayout.NORTH);
        box.add(quit, BorderLayout.SOUTH);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
        getContentPane().add(box);
        pack();
        setVisible(true);
    }

    public static void main(String args[]) {
        swhello app = new swhello();
    }
}
