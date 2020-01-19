import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.Math;
import javax.swing.*;

public class Kreuzw extends JFrame {

    public static void main(String[] args) {
        new Kreuzw();        //main method and instantiating tic tac object and calling initialize function
    }

    private JFrame frame = new JFrame("kreuzw");
    private JTextField[][] tfs;
    String [][]in;
    //Node [][]layout;

    private JTextField tf0 = new JTextField();
    private JTextField tf1 = new JTextField();

    private JPanel mainPanel = new JPanel(new BorderLayout());
    private JPanel menu;

    private JButton yes;
    private JButton yes2;

    private Kreuzw() {
        super();
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(EXIT_ON_CLOSE);        //Setting dimension of JFrame and setting parameters
        frame.setVisible(true);
        frame.setResizable(true);
        initialize();//for buttons and so on
    }

    private void initialize()             //Initialize tic tac toe gui
    {
        frame.add(mainPanel);                                         //add main container panel to frame
        //mainPanel.setPreferredSize(new Dimension(500, 500));
        menu = new JPanel(new GridLayout(2, 2));
        //menu.setPreferredSize(new Dimension(500, 500));
        mainPanel.add(menu, BorderLayout.CENTER);

        menu.add(tf0);
        menu.add(tf1);

        yes = new JButton();
        menu.add(yes);
        yes.setText("Yes");
        yes.setVisible(true);
        yes.setEnabled(true);
        yes.addActionListener(new myActionListener());
    }

    private void makeTfs(int x,int y) {

        menu.setVisible(false);
        menu = new JPanel(new GridLayout(y+1, x));
        //menu.setPreferredSize(new Dimension(500, 500));
        mainPanel.add(menu, BorderLayout.CENTER);
        tfs=new JTextField[y][x];
        for (int i = 0; i < tfs.length; i++)
        {
            for (int j = 0; j < tfs[0].length; j++)
            {
                tfs[i][j] = new JTextField();
                menu.add(tfs[i][j]);
            }
        }
        yes2 = new JButton();
        menu.add(yes2);
        yes2.setText("Yes");
        yes2.setVisible(true);
        yes2.setEnabled(true);
        yes2.addActionListener(new myActionListener());
    }

    private void yes() {
        String x=tf0.getText();
        String y=tf1.getText();
        if(makenum(x)>0&&makenum(y)>0)
        {

            makeTfs(makenum(x),makenum(y));
        }
    }

    private void yes2() {

        in=new String [tfs.length][tfs[0].length];
        for (int i = 0; i < tfs.length; i++)
        {
            for (int j = 0; j < tfs[0].length; j++)
            {
                in[i][j]=tfs[i][j].getText();
            }
        }

        out2(in);


    }

    private int makenum(String s)
    {
        try
        {
            return Integer.parseInt(s);
        }
        catch (NumberFormatException nfe)
        {
            return -1;
        }
    }



    private class myActionListener implements ActionListener {      //Implementing action listener for buttons
        public void actionPerformed(ActionEvent a) {
            if (a.getSource() == yes) {
                yes();
            }
            if (a.getSource() == yes2) {
                yes2();
            }
        }

    }

    public void out2(String[][] o)
    {
        System.out.println("{");
        for(int i=0;i<o[0].length-1;i++)
        {
            System.out.print("{");
            for(int j=0;j<o.length-1;j++)
            {
                System.out.print(o[j][i]+", ");
            }
            System.out.print(o[o.length-1][i]);
            System.out.println("},");
        }
        System.out.print("{");
        for(int j=0;j<o.length-1;j++)
        {
            System.out.print(o[j][o[0].length-1]+", ");
        }
        System.out.print(o[o.length-1][o[0].length-1]);
        System.out.println("}");
        System.out.println("}");
    }
}