import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int a, b, c;
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int ans;
        int[] mx = new int[3];

        if (a == b && b == c && c == a){
            ans = 10000 + a * 1000;
        }
        else if (a != b && b != c && c != a){
            mx[0] = a;
            mx[1] = b;
            mx[2] = c;
            Arrays.sort(mx);
            ans = 100 * mx[2];
        }
        else{
            if(a == b || a == c){
                ans = a;
            }
            else {
                ans = b;
            }
            ans = 1000 + ans * 100;
        }
        System.out.println(ans);
    }
}
