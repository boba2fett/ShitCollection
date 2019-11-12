import java.util.*;
public class MatrixenLOL
{

    String [][] m=new String[16][16];

    public MatrixenLOL()
    {
        for(int i=0;i<m.length;i++)
        {
            Arrays.fill(m[i], "0");
        }
    }

    public void generateKing()
    {
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
            {
                setNeighboursKing(x,y);
            }
        }
    }

    public void setNeighboursKing(int x,int y)
    {
        ArrayList<Integer> fields=new ArrayList<Integer>();
        for(int xx=x-1;xx<=x+1;xx++)
        {
            for(int yy=y-1;yy<=y+1;yy++)
            {
                if(xx==x&&yy==y)
                {
                    continue;
                }
                if(xx<0||xx>=4)
                {
                    continue;
                }
                if(yy<0||yy>=4)
                {
                    continue;
                }
                fields.add(coordsToNum(xx,yy));
            }
        }
        for (int num : fields)
        {
            m[num][coordsToNum(x,y)]="Fraction(1,"+fields.size()+")";//wohin|woher
        }
    }

    public void generateQueen()
    {
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
            {
                setNeighboursQueen(x,y);
            }
        }
    }

    public void setNeighboursQueen(int x,int y)
    {
        ArrayList<Integer> fields=new ArrayList<Integer>();
        for(int xx=0;xx<4;xx++)
        {
            for(int yy=0;yy<4;yy++)
            {
                if(xx==x&&yy==y)
                {
                    continue;
                }

                if(yy==y||xx==x||Math.abs(xx-x)==Math.abs(yy-y))
                {
                    fields.add(coordsToNum(xx, yy));
                }
            }
        }
        for (int num : fields)
        {
            m[num][coordsToNum(x,y)]="Fraction(1,"+fields.size()+")";//wohin|woher
        }
    }

    public void generateTower()
    {
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
            {
                setNeighboursTower(x,y);
            }
        }
    }

    public void setNeighboursTower(int x,int y)
    {
        ArrayList<Integer> fields=new ArrayList<Integer>();
        for(int xx=0;xx<4;xx++)
        {
            for(int yy=0;yy<4;yy++)
            {
                if(xx==x&&yy==y)
                {
                    continue;
                }

                if(yy==y||xx==x)
                {
                    fields.add(coordsToNum(xx, yy));
                }
            }
        }
        for (int num : fields)
        {
            m[num][coordsToNum(x,y)]="Fraction(1,"+fields.size()+")";//wohin|woher
        }
    }

    public void generateWalker()
    {
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
            {
                setNeighboursWalker(x,y);
            }
        }
    }

    public void setNeighboursWalker(int x,int y)
    {
        ArrayList<Integer> fields=new ArrayList<Integer>();
        for(int xx=0;xx<4;xx++)
        {
            for(int yy=0;yy<4;yy++)
            {
                if(xx==x&&yy==y)
                {
                    continue;
                }

                if(Math.abs(xx-x)==Math.abs(yy-y))
                {
                    fields.add(coordsToNum(xx, yy));
                }
            }
        }
        for (int num : fields)
        {
            m[num][coordsToNum(x,y)]="Fraction(1,"+fields.size()+")";//wohin|woher
        }
    }

    public void generateJumper()
    {
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
            {
                setNeighboursJumper(x,y);
            }
        }
    }

    public void setNeighboursJumper(int x,int y)
    {
        ArrayList<Integer> fields=new ArrayList<Integer>();
        for(int xx=x-2;xx<=x+2;xx++)
        {
            for(int yy=y-2;yy<=y+2;yy++)
            {
                if(xx==x||yy==y)
                {
                    continue;
                }
                if(xx<0||xx>=4)
                {
                    continue;
                }
                if(yy<0||yy>=4)
                {
                    continue;
                }
                if(Math.abs(xx-x)==Math.abs(yy-y))
                {
                    continue;
                }
                fields.add(coordsToNum(xx, yy));
            }
        }
        for (int num : fields)
        {
            m[num][coordsToNum(x,y)]="Fraction(1,"+fields.size()+")";//wohin|woher
        }
    }

    public int coordsToNum(int x,int y)
    {
        return 4*y+x;
    }

    public void out()
    {
        System.out.println("[");
        for(int i=0;i<m.length-1;i++)
        {
            Oneout(m[i]);
            System.out.println(",");
        }
        Oneout(m[m.length-1]);
        System.out.println();
        System.out.println("]");
    }

    public void Oneout(String []o)
    {
        System.out.print("[");
        for(int i=0;i<o.length-1;i++)
        {
            System.out.print(o[i]+",");
        }
        System.out.print(o[o.length-1]);
        System.out.print("]");
    }

    public static void main(String args[])
    {
        MatrixenLOL m=new MatrixenLOL();
        m.generateJumper();
        m.out();
    }
}
