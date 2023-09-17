import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine(), " ");
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		int cnt = 0;
		boolean flag = true;
		Loop:
		for (int last = N - 1; last > 0; last--) {
			for (int i = 0; i < last; i++) {
				if (arr[i] > arr[i + 1]) {
					cnt++;
					int tmp = arr[i];
					arr[i] = arr[i + 1];
					arr[i + 1] = tmp;
					if (cnt == K) {
						flag = false;
						System.out.println(arr[i] + " " + arr[i + 1]);
						break Loop;
					}
				}
			}
		}
		if (flag) {
			System.out.println(-1);
		}
	}
}