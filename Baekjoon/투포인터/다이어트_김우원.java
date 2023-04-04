import java.util.PriorityQueue;
import java.util.Scanner;
/*
[1484] 다이어트
 */
public class 다이어트_김우원 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int G = sc.nextInt();
        PriorityQueue<Long> pq = new PriorityQueue<>();
        long be = 1;
        long af = 1;
        while (true) {
            long diff = (af * af) - (be * be);
            if (diff == G) {
                pq.add(af);
                af++;
            } else if (diff < G) af++;
            else if (af - be == 1) break;
            else be++;
        }
        if(pq.isEmpty()) System.out.println(-1);
        else while (!pq.isEmpty()) System.out.println(pq.poll());
    }

}
