import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N - i - 1; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 2 * i + 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = N; i < 2 * N - 1; i++) {
            for (int j = 0; j < i - N + 1; j++) {
                System.out.print(" ");
            }
            for (int k = 0; k < 4 * N - 2 * i - 3; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}