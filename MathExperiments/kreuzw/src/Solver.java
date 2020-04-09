import java.util.ArrayList;

public class Solver
{
    Node[][]nds;
    public void redin(String in[][])
    {
        nds=new Node [in.length][in[0].length];

        for (int i = 0; i < in.length; i++)
        {
            for (int j = 0; j < in[0].length; j++)
            {
                if(in[i][j].contains("="))
                {
                    nds[i][j]=new Node(true);
                }
                else
                {
                    boolean r = in[i][j].contains("r");
                    boolean l = in[i][j].contains("l");
                    boolean u = in[i][j].contains("u");
                    boolean d = in[i][j].contains("d");
                    nds[i][j] = new Node(r, l, u, d);
                }
            }
        }
    }

    public String[][] solve()
    {
        //String [][]save=new String[nds.length][nds[0].length];
        for (int i = 0; i < nds.length; i++)
        {
            for (int j = 0; j < nds[0].length; j++)
            {

            }
        }
        return new String[1][1];
    }

    public void classify()
    {
        int count=0;
        for (int i = 0; i < nds.length; i++)
        {
            for (int j = 0; j < nds[0].length; j++)
            {
                if(nds[i][j].staysEmpty())
                {
                    nds[i][j].addNum(count);
                    if(nds[i][j].getR())
                    {
                        classify(i, j, 1, 0, count);
                    }
                    if(nds[i][j].getL())
                    {
                        classify(i, j, -1, 0, count);
                    }
                    if(nds[i][j].getD())
                    {
                        classify(i, j, 0, 1, count);
                    }
                    if(nds[i][j].getU())
                    {
                        classify(i, j, 0, -1, count);
                    }
                }
            }
        }
    }

    public void classify(int x,int y, int xDirection, int yDirection,int classify)
    {
        do
        {
            x+=xDirection;
            y+=yDirection;
            nds[x][y].addNum(classify);
        }
        while(!nds[x][y].staysEmpty());
    }
}
