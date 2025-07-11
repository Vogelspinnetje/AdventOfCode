import java.io.IOException;
import java.util.List;

public class AoC_01_2020 {
    public static void main(String[] args) throws IOException {
        List<String> input = Util.readInput("inputs/AoC_01_2020.txt");
        int comparator1;
        int comparator2;
        int base;
        int answer1 = 0;
        int answer2 = 0;

        for (int i = 0; i < input.size(); i++){
            base = Integer.parseInt(input.get(i));

            for (int j = i; j < input.size(); j ++){
                if (i == j) continue;

                comparator1 = Integer.parseInt(input.get(j));

                if (base + comparator1 == 2020) {
                    answer1 = base * comparator1;
                }

                for (int k = j; k < input.size(); k ++){
                    if (k == j) continue;

                    comparator2 = Integer.parseInt(input.get(k));

                    if (base + comparator1 + comparator2 == 2020) {
                        answer2 = base * comparator1 * comparator2;
                    }
                }
            }
        }

        System.out.println(answer1 + ", " + answer2);
    }
}
