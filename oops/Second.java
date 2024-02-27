import java.util.Arrays;
import java.util.Scanner;

public class Second {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[10];

        System.out.println("Enter 10 Digits");

        for(int i = 0; i < 10; i++){
            while(true){
                try {
                    arr[i] = scanner.nextInt();
                    break;
                } catch (Exception err) {
                    System.out.println("Invalid Input " + err.getMessage());
                    scanner.nextLine();
                }
            }
        }

        Arrays.sort(arr);
        for(int i = 9; i >= 0; i--){
            System.out.println(arr[i]);
        }
    }
}
