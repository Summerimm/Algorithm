import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String[] S = br.readLine().split(" ");  // 공백 분리

            int len = Integer.parseInt(S[0]); // String에서 int형으로 변환
            String str = S[1];

            for (int j = 0; j < str.length(); j++) {
                for (int k = 0; k < len; k++) {
                    System.out.print(str.charAt(j));
                }
            }
            System.out.println();
        }
    }
}