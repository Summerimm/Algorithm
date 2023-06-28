import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int r;
        int q = 1;

        while (q != 0) {
            q = N / B;
            r = N % B;
            N  = q;
            if (r <= 9) {
                sb.append(r);
            } else {
                r += 55;
                char rtmp = (char) r;
                sb.append(rtmp);
            }
        }
        System.out.println(sb.reverse());
    }
}