import java.util.Scanner;

public class Main {
    public static boolean[] prime;
    public static void 에라토스테네스의체_양석진(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        make_prime(N);

        for(int i = 0; i < prime.length; i++) {
            if(prime[i] == false) {
                System.out.println(i);
            }
        }
    }

    public static void make_prime(int N) {
        prime = new boolean[N + 1];

        if(N < 2) {
            return;
        }

        prime[0] = prime[1] = true;

        for(int i = 2; i <= Math.sqrt(N); i++) {

            if(prime[i] == true) {
                continue;
            }

            for(int j = i * i; j < prime.length; j = j+i) {
                prime[j] = true;
            }
        }
    }
}