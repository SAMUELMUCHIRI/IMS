public class variablej {
    /* naming a new type */
    enum DAY {SUNDAY , MONDAY , TUSDAY, WEDNESDAY, THURSDAY,FRIDAY,SATURDAY}
    public static void main(String[] args){
        /* declaring variables  */
        double princ_iple;
        double finale;
        double rate;
        double time;
        String cate;
        DAY Day;
        String joke;

        cate="seize the day ";
        Day=DAY.SUNDAY ;

        princ_iple =40000;
        rate = 0.3 ;
        time=3;
        joke=(System.in("time"));
        
        finale= princ_iple * rate * time;
        System.out.println(Math.sqrt(finale));
        System.out.println(finale);
        System.out.printf( "%1.2f",finale);
        System.out.println(cate.toUpperCase()+" "+ Day);




    }

}