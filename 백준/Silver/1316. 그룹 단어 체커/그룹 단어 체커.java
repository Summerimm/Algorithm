import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;

public class Main {
    // BufferedReader은 예외로 IOException을 던지므로
    // 반드시 입력이 들어가는 함수 (main, check) 옆에 throws IOException 을 써주어야 한다.
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int count = 0; // 그룹 단어의 개수
        int N = Integer.parseInt(br.readLine()); // 단어의 개수 N

        for (int i = 0; i < N; i++) {
            if (check()) { // 그룹단어면 count +1
                count++;
            }
        }
        System.out.println(count);
    }

    public static boolean check() throws IOException {
        boolean[] check = new boolean[26]; // 알파벳 배열
        int prev = 0; // 이전 알파벳
        String str = br.readLine();

        for (int i = 0; i < str.length(); i++) {
            int now = str.charAt(i); // 현재 알파벳

            if (prev != now) { // 앞의 알파벳과 같으면 연산 pass, 다를 때만 연산
                if (!check[now - 'a']) { // 이전에 해당 알파벳 체크된 적이 없음
                    check[now - 'a'] = true;
                    prev = now;
                } else { // 이전에 해당 알파벳 체크된 적이 있음
                    return false;
                }
            }
        }
        return true;
    }
}