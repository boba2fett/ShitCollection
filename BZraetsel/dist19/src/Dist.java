import java.util.ArrayList;
import java.util.Arrays;

public class Dist
{
    public Dist()
    {

    }

    public static void main(String args[])
    {
        Dist d=new Dist();
        d.main();
    }

    final int[][]save=new int[6][3];
    final int[][]save2=new int[6][3];

    public void main()
    {
        int counter=0;
        final int[][]et=constET();
        int[][]a=new int[6][3];
        for(int i=0;i<a.length;i++)
        {
            Arrays.fill(a[i],0);
        }
        a[0][0]=14;
        a[0][1]=4;
        setSave(a);

        for(int z=0;z<32;z++)
        {
            boolean []barr=toBinary(z,5);
            for (int i = 0; i < et.length; i++)//i=element to skip
            {
                a=getSave();
                int ii=0;
                for(int j=1;j<a.length;j++)
                {
                    if(j-1==i)
                    {
                        ii++;
                    }
                    if(barr[j-1])
                    {
                        a[j][0] = et[ii][0];
                        a[j][1] = et[ii][1];
                    }
                    else
                    {
                        a[j][1] = et[ii][0];
                        a[j][0] = et[ii][1];
                    }
                    ii++;
                }
                setSave2(a);
                int[]max={4,4,4,4,4};
                int[]count={0,0,0,0,0};
                boolean breaked=false;
                while(!breaked)
                {
                    count[4]++;
                    if (count[4] > max[4])
                    {
                        count[4] = 0;
                        count[3]++;
                        if (count[3] > max[3])
                        {
                            count[3] = 0;
                            count[2]++;
                            if (count[2] > max[2])
                            {
                                count[2] = 0;
                                count[1]++;
                                if (count[1] > max[1])
                                {
                                    count[1] = 0;
                                    count[0]++;
                                    if (count[0] > max[0])
                                    {
                                        breaked=true;
                                    }
                                }
                            }
                        }
                    }
                    if(!legit(count)||breaked)
                    {
                        continue;
                    }
                    a=getSave2();
                    int[][]s=getSave2();
                    for(int c=0;c<count.length;c++)
                    {
                        a[1+c]=s[count[c]+1];
                    }
                    makeRest(a);
                    counter++;
                    if(a[0][0]!=-1)
                    {
                        if(check(a))
                        {
                            out2(a);
                        }
                    }
                }
            }
        }
        System.out.println(counter);//23040=2^5*5!*6
    }

    private boolean legit(int[]a)
    {
        for (int i=0;i<a.length;i++)
        {
            for (int j=i+1;j<a.length;j++)
            {
                if(a[i]==a[j])
                {
                    return false;
                }
            }
        }
        return true;
    }





    private int[][]makeRest(int[][]a)
    {
        ArrayList<Integer> donts=new ArrayList<Integer>();
        donts.add(6);

        for (int i=0;i<a.length;i++)
        {
            donts.add(a[i][0]);
            donts.add(a[i][1]);
        }

        for (int i=0;i<a.length-1;i++)
        {
            int val=24-a[i][1]-a[i+1][1];
            if(donts.indexOf(val)==-1&&val>0&&val<20)
            {
                a[i][2]=val;
                donts.add(val);
            }
            else
            {
                a[i][2]=val;
                a[0][0]=-1;
                return a;
            }
        }
        int val=a[a.length-1][2]=24-a[a.length-1][1]-a[0][1];
        if(donts.indexOf(val)==-1&&val>0&&val<20)
        {
            a[a.length-1][2] =val;
            donts.add(val);
        }
        else
        {
            a[0][2]=val;
            a[0][0]=-1;
            return a;
        }
        return a;
    }

    private boolean check(int[][]a)
    {
        for (int i=0;i<a.length-1;i++)
        {
            if(24!=a[i][1]+a[i+1][1]+a[i][2])
            {
                return false;
            }
            if(24!=6+a[i][0]+a[i][1])
            {
                return false;
            }
        }
        if(24!=a[a.length-1][1]+a[0][1]+a[a.length-1][2])
        {
            return false;
        }
        if(24!=6+a[a.length-1][0]+a[a.length-1][1])
        {
            return false;
        }
        ArrayList<Integer> nums=new ArrayList<Integer>();
        for(int i=0;i<a.length;i++)
        {
            for(int j=0;j<a[0].length;j++)
            {
                nums.add(a[i][j]);
            }
        }
        nums.add(6);
        for(int i=1;i<20;i++)
        {
            if(nums.indexOf(i)==-1)
            {
                return false;
            }
        }

        return true;
    }


    private int[][] constET()
    {
        int[][]et=new int [6][2];//eighteens
        int val=1;
        for(int i=0;i<6;i++)
        {
            if(val==4||val==6)
            {
                val++;
            }
            et[i][0]=val;
            et[i][1]=18-val;
            val++;
        }
        return et;
    }

    public void out2(int[][] o)
    {
        System.out.println("[");
        for(int i=0;i<o[0].length-1;i++)
        {
            System.out.print("[");
            for(int j=0;j<o.length-1;j++)
            {
                System.out.print(o[j][i]+", ");
            }
            System.out.print(o[o.length-1][i]);
            System.out.println("],");
        }
        System.out.print("[");
        for(int j=0;j<o.length-1;j++)
        {
            System.out.print(o[j][o[0].length-1]+", ");
        }
        System.out.print(o[o.length-1][o[0].length-1]);
        System.out.println("]");
        System.out.println("]");
    }

    private boolean[] toBinary(int number, int base) {
        final boolean[] ret = new boolean[base];
        for (int i = 0; i < base; i++) {
            ret[base - 1 - i] = (1 << i & number) != 0;
        }
        return ret;
    }

    private int[][]getSave()
    {
        int[][]a=new int[6][3];
        for (int i=0;i<a.length;i++)
        {
            for (int j=0;j<a[0].length;j++)
            {
                a[i][j]=save[i][j];
            }
        }
        return a;
    }

    private void setSave(int[][]a)
    {
        for (int i=0;i<a.length;i++)
        {
            for (int j=0;j<a[0].length;j++)
            {
                save[i][j]=a[i][j];
            }
        }
    }

    private int[][]getSave2()
    {
        int[][]a=new int[6][3];
        for (int i=0;i<a.length;i++)
        {
            for (int j=0;j<a[0].length;j++)
            {
                a[i][j]=save2[i][j];
            }
        }
        return a;
    }

    private void setSave2(int[][]a)
    {
        for (int i=0;i<a.length;i++)
        {
            for (int j=0;j<a[0].length;j++)
            {
                save2[i][j]=a[i][j];
            }
        }
    }
}
