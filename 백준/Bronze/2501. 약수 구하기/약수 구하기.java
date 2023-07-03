import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int tmp = 0; // 몇 번째로 작은 약수인지 저장
        int fac = 0; // 약수
        while (tmp < K && fac < N) {
            fac++;
            if (N % fac == 0) {
                tmp++;
            }
        }
        if (tmp == K) {
            System.out.println(fac);
        } else {
            System.out.println(0);
        }
    }
}