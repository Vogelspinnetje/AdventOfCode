import java.io.IOException;
import java.util.List;

public class AoC_01_2020 {
    public static void main(String[] args) throws IOException {
        List<String> input = Util.readInput("inputs/AoC_01_2020.txt");
        int comparator;
        int base;
        int answer1 = 0;
        boolean break_loop = false;

        for (int i = 0; i < input.size(); i++){
            if (break_loop) break;
            base = Integer.parseInt(input.get(i));

            for (int j = i; j < input.size(); j ++){
                if (i == j) continue;
                if (break_loop) break;

                comparator = Integer.parseInt(input.get(j));

                if (base + comparator == 2020) {
                    answer1 = base * comparator;
                    break_loop = true;
                }
            }
        }

        System.out.println(answer1);
    }
}
