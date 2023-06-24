import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double totalCnt = 0;
        double gradeCnt = 0;
        double add = 0;
        for (int i = 0; i < 20; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            String subject = st.nextToken();
            double cnt = Float.parseFloat(st.nextToken());
            String grade = st.nextToken();

            switch (grade) {
                case "A+": add = 4.5 * cnt; break;
                case "A0": add = 4.0 * cnt; break;
                case "B+": add = 3.5 * cnt; break;
                case "B0": add = 3.0 * cnt; break;
                case "C+": add = 2.5 * cnt; break;
                case "C0": add = 2.0 * cnt; break;
                case "D+": add = 1.5 * cnt; break;
                case "D0": add = 1.0 * cnt; break;
                case "F": add = 0; break;
            }

            if (grade.equals("P")) {
                cnt = 0;
            } else {
                gradeCnt += add;
            }
            totalCnt += cnt;
        }
        System.out.println(gradeCnt / totalCnt);
    }
}