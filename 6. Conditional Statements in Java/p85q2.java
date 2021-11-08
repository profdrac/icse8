//WAP to get three numbers and show the largest and smallest number

class p85q2
{
    public static void main(int a, int b, int c)
    {
        //check for bigger number
        if(a>b && a>c)
        {
            System.out.println(a+" is greatest");
        }
        else if(b>a && b>c)
        {
            System.out.println(b+" is greatest");
        }
        else
        {
            System.out.println(c+" is greatest");
        }
        //now check for smaller number
        if(a<b && a<c)
        {
            System.out.println(a+" is smallest");
        }
        else if(b<a && b<c)
        {
            System.out.println(b+" is smallest");
        }
        else
        {
            System.out.println(c+" is smallest");
        }
    }
}