import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int t = sc.nextInt();

        int q = t / 60;
        int r = t % 60;
        h += q;
        m += r;
        if (m >= 60){
            m -= 60;
            h ++;
        }
        if (h > 23){
            h -= 24;
        }
        System.out.println(h + " " + m);
    }
}
