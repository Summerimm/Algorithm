import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = b;

        for (int i=0;i<3;i++){
            int r = b % 10;
            b /= 10;
            System.out.println(a * r);
        }
        System.out.println(a * c);
    }
}
