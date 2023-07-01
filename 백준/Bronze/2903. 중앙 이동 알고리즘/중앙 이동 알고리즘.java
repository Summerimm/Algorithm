import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 2의 제곱 - 2*2-1의 제곱 - 3* 2-1의 제곱
        // 0일 때 2, 4
        // 1일 때 3, 9
        // 2일 때 5, 25
        // 3일 때 9, 81
        // 4일 때 17, 289
        // 5일 때 33, 1089
        
        int N = Integer.parseInt(br.readLine());
        double k = 2; // 제곱할 수
        double ans = 0;
        
        for (int i = 0; i < N; i++) {
            k = k * 2 - 1;
            ans = Math.pow(k, 2);
        }
        System.out.println((int) ans);
    }
}