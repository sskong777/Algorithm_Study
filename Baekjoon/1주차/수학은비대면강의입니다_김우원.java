import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 수학은비대면강의입니다_김우원 {//[19532] 수학은 비대면 강의입니다
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int[] nums = new int[6];
        for(int i = 0; i < 6; i++) nums[i] = Integer.parseInt(input[i]);
        int[] ans = new int[2];
        out : for(int x = -999; x <= 999; x++) {
            for(int y = -999; y <= 999; y++) {
                if(nums[0] * x + nums[1] * y == nums[2] && nums[3] * x + nums[4] * y == nums[5]) {
                    ans[0] = x;
                    ans[1] = y;
                    break out;
                }
            }
        }
        System.out.println(ans[0] + " " + ans[1]);
    }
}
