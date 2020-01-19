import java.util.ArrayList;

public class Node
{
    boolean r=false;
    boolean l=false;
    boolean u=false;
    boolean d=false;
    boolean stayEmpty=false;
    ArrayList<Integer> nums=new ArrayList<Integer>();

    public Node(boolean r,boolean l,boolean u, boolean d)
    {
        this.r=r;
        this.l=l;
        this.u=u;
        this.d=d;
        stayEmpty=true;
    }

    public Node(boolean stayEmpty)
    {
        this.stayEmpty=true;
    }

    public boolean staysEmpty()
    {
        return stayEmpty;
    }

    public void  addNum(int num)
    {
        nums.add(num);
    }

    public ArrayList<Integer> getNums()
    {
        return nums;
    }

    public boolean getR()
    {
        return r;
    }

    public boolean getL()
    {
        return l;
    }

    public boolean getU()
    {
        return u;
    }

    public boolean getD()
    {
        return d;
    }
}
