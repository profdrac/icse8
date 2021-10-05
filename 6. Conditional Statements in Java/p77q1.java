//WAP to convert grams to kgs and remaining grams
class p77q1
{
    public static void main()
    {
        int grams = 3420;
        int kgs = grams/1000;
        int remaining = grams%1000;
        System.out.println(kgs+" Kilograms and "+remaining+" grams");
    }
}