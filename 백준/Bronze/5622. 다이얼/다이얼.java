import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int cnt = 0;
        int len = str.length();

        for (int i = 0; i < len; i++) {

            switch (str.charAt(i)) {
                case 'A': case 'B': case 'C':
                    cnt += 3;
                    break;

                case 'D': case 'E': case 'F':
                    cnt += 4;
                    break;

                case 'G': case 'H': case 'I':
                    cnt += 5;
                    break;

                case 'J': case 'K': case 'L':
                    cnt += 6;
                    break;

                case 'M': case 'N': case 'O':
                    cnt += 7;
                    break;

                case 'P': case 'Q': case 'R': case 'S':
                    cnt += 8;
                    break;

                case 'T': case 'U': case 'V':
                    cnt += 9;
                    break;

                case 'W': case 'X': case 'Y': case 'Z':
                    cnt += 10;
                    break;
            }
        }
        System.out.println(cnt);
    }
}