import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		String formula = br.readLine();
        
		double[] arr = new double[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Double.parseDouble(br.readLine());
		}

		Stack<Double> stack = new Stack<>();

		double ans = 0;
		for (int i = 0; i < formula.length(); i++) {
			if ('A' <= formula.charAt(i) && formula.charAt(i) <= 'Z') {
				stack.push(arr[formula.charAt(i) - 'A']);
			} else {
				double operand2 = stack.pop();
				double operand1 = stack.pop();
				switch (formula.charAt(i)) {
					case '+':
						ans = operand1 + operand2;
						stack.push(ans);
						break;
					case '-':
						ans = operand1 - operand2;
						stack.push(ans);
						break;
					case '*':
						ans = operand1 * operand2;
						stack.push(ans);
						break;
					case '/':
						ans = operand1 / operand2;
						stack.push(ans);
						break;
				}
			}
		}
		System.out.printf("%.2f", stack.pop());
	}
}