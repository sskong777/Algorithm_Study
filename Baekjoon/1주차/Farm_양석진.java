import java.io.*;
import java.util.*;
public class Farm_양석진{
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        ArrayList<Integer> result_x = new ArrayList<>();
        ArrayList<Integer> result_y = new ArrayList<>();


        for(int x = 1; x<=1000; x++){
            for(int y=1; y<=1000; y++){
                if(a * x + b * y == w){
                    if(x + y == n) {
                        result_x.add(x);
                        result_y.add(y);
                        break;
                    }
                }
            }
        }

        if(result_x.size() > 1){
            bw.write("-1");
        } else if(result_x.isEmpty()){
            bw.write("-1");
        } else{
            bw.write(result_x.get(0) + " " + result_y.get(0));
        }
        bw.close();
    }
}