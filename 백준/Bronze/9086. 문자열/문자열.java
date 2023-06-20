import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        String S;
        for (int i = 0; i < T; i++) {
            S = br.readLine();
            sb.append(S.charAt(0));
            sb.append(S.charAt(S.length()-1) + "\n");
        }
        System.out.println(sb);
    }
}