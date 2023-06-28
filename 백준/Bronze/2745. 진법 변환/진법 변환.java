import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String N = st.nextToken();
        int B = Integer.parseInt(st.nextToken());
        int len = N.length();
        int ans = 0;

        for (int i = len - 1; i > -1; i--) {
            int c;
            if (N.charAt(i) <= '9') {
                c = N.charAt(i) - '0';
            } else {
                c = N.charAt(i) - 55;
            }
            ans += c * (Math.pow(B, len - i - 1));
        }
        System.out.println(ans);
    }
}