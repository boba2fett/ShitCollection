import java.util.Arrays;

public class Permutator
{
    int val=0;
    int base;
    int length;
    public Permutator(int base,int length)
    {
        this.base=base;
        this.length=length;
    }

    public int[] next()
    {
        int in=val++;
        int[]arr=new int[length];
        Arrays.fill(arr,0);
        for(int i=arr.length-1;in != 0&&i>=0;i--)
        {
            arr[i] = in % base;
            in -= arr[i];
            in /= base;
        }
        return arr;
    }

    public boolean maxReached()
    {
        return val>=calcMax(length,base);
    }


    public static boolean rebase(int in,int toBase,int[]arr)
    {
        Arrays.fill(arr,0);
        for(int i=arr.length-1;in != 0&&i>=0;i--)
        {
            arr[i] = in % toBase;
            in -= arr[i];
            in /= toBase;
        }
        return in==0;
    }


    public static boolean[] toBooleanArray(int number, int base) {
        final boolean[] ret = new boolean[base];
        for (int i = 0; i < base; i++) {
            ret[base - 1 - i] = (1 << i & number) != 0;
        }
        return ret;
    }

    public static int eval(int in[],int from)
    {
        int val=0;
        for(int i=1;i<=in.length;i--)
        {
            val+=in[in.length-i]*Math.pow(from,i);
        }
        return val;
    }

    public static int calcMax(int length,int toBase)
    {
        return (int)Math.pow(toBase,length);
    }

    public static void main(String args[])
    {
        int base=3;
        int length=2;
        int[]a=new int[length];
        for(int i=0;i<calcMax(length,base);i++)
        {
            rebase(i,base,a);
            out(a);
        }

        Permutator p=new Permutator(base, length);
        while (!p.maxReached())
        {
            out(p.next());
        }
    }

    public static void out(int[]o)
    {
        System.out.print("{");
        for(int j=0;j<o.length-1;j++)
        {
            System.out.print(o[j]+", ");
        }
        System.out.print(o[o.length-1]);
        System.out.println("}");
    }
}
