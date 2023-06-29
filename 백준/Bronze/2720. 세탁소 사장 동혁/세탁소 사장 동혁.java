import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int q = 0;
            int d = 0;
            int n = 0;
            int p = 0;
            int charge = Integer.parseInt(br.readLine());
            while (charge != 0) {
                if (charge >= 25) {
                    q = charge / 25;
                    charge %= 25;
                } else if (charge >= 10) {
                    d = charge / 10;
                    charge %= 10;
                } else if (charge >= 5) {
                    n = charge / 5;
                    charge %= 5;
                } else {
                    p = charge / 1;
                    charge %= 1;
                }
            }
            System.out.println(q + " " + d + " " + n + " " + p);
        }
    }
}