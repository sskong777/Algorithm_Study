import java.util.Scanner;

public class 나무자르기_서명현 {
    public static void main(String[] args)   {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[] trees = new int[n];
        int MAX = 0;
        for (int i = 0; i < n; i++) {
            trees[i] = scan.nextInt();
            if (trees[i]>MAX) {
                MAX = trees[i];
            }
        }
        scan.close();

        int low = 0;
        int high = MAX;
        int H = 0;
        while (low<=high) {
            int mid = (low+high) / 2;
            long count = 0; //gained trees
            for (int tree : trees) {
                if(tree > mid)
                    count+= (tree - mid);
            }
            if (m <= count) {
                low = mid + 1;
                if(mid >= H) //higher the better
                    H = mid;
            }
            else{
                high = mid - 1;
            }
        }
        System.out.println(H);
    }
}
