import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str1 = br.readLine();
        String str2 = new StringBuilder(str1).reverse().toString();
        if (str1.equals(str2)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}