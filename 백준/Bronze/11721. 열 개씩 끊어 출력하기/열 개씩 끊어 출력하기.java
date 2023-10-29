import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String st = br.readLine();

		int tmp = 0;
		for (int i = 0; i < st.length(); i++) {
			char c = st.charAt(i);
			System.out.print(c);
			tmp++;
			if (tmp == 10 && i != st.length() - 1) {
				System.out.println();
				tmp = 0;
			}
		}
	}
}