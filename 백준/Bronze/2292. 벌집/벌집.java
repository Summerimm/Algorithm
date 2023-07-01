import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1 - 1: 1개
        // 2 - 2~7: 6개
        // 3 - 8~19: 12개
        // 4 - 20~37: 18개

        int N = Integer.parseInt(br.readLine());
        int num = 1; // 그 열까지 최대 번호
        int ans = 1;
        while (num < N) {
            num += 6 * ans;
            ans++;
        }
        System.out.println(ans);
    }
}