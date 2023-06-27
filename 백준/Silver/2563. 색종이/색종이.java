import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        int ans = 0;
        boolean[][] arr = new boolean[101][101];

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            for (int j = N; j < N + 10; j++) {
                for (int k = M; k < M + 10; k++) {
                    if (!arr[j][k]) {
                        arr[j][k] = true;
                        ans ++;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}