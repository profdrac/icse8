//WAP to convert seconds to hours, minutes and seconds

class hms
{
    public static void main(int sec)
    {
        int h = sec/3600;
        sec = sec % 3600;
        int m = sec/60;
        sec = sec % 60;
        System.out.println(h+" hours "+m+" minutes and "+sec+" seconds");
    }
}